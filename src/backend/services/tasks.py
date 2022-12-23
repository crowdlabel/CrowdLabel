import schemas.questions
from utils.datetime_str import datetime_now_str
from datetime import datetime

from services.database import engine
import models.task
import models.user
import models.answer
import models.question
from sqlalchemy.orm import sessionmaker, scoped_session, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_ ,or_
conection = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

import pathlib

import schemas.tasks
import schemas.users
import schemas.answers
import json
import patoolib
from utils.config import get_config
TASK_UPLOAD_DIR = pathlib.Path(get_config('file_locations.tasks'))

from services.users import user_service
from services.questions import question_service

import asyncio



class Tasks:

    def __init__(self):
        pass


    async def create_task(self,
        requester: schemas.users.Requester,
        task_request: schemas.tasks.CreateTaskRequest,
        resource_path: pathlib.Path    
    ) -> schemas.tasks.Task | str:
        con = scoped_session(conection)
        if task_request.responses_required <= 0:
            return '`responses_required` must be positive'
        if task_request.credits < 0:
            return '`credits` must be positive'

        response = await user_service.handle_transaction(
            schemas.users.TransactionRequest(amount=- task_request.credits * task_request.responses_required),
            user=requester
        )
        if not isinstance(response, float):
            await asyncio.shield(con.close())
            return response

        # TODO: which task_id to use?

        info = task_request.dict()
        del info['questions']
        task_schema = schemas.tasks.Task(**info, 
            task_id= 0,
            requester=requester.username,
            date_created=datetime.utcnow(),
            resource_path=resource_path
        )

        for question in task_request.questions:
            task_schema.questions.append(question)
        missing = []
        for question in task_schema.questions:
            if not question.resource:
                continue
            if not pathlib.Path(resource_path / question.resource).is_file():
                missing.append(str(question.resource))

        if missing:
            await asyncio.shield(con.close())
            return 'The following resources are missing: ' + ', '.join(missing)


        task = models.task.Task(task_schema,
            resource_path=str(resource_path)
        )
        
       
        async with con.begin():
            target = await con.execute(select(models.user.Requester)
                .where(models.user.Requester.username==requester.username).options(selectinload(models.user.Requester.task_requested)))
            res = target.scalars().first()
            if res == None:
                return 'requester not found'
            task.requester_id = res.id
            res.task_requested.append(task)
            con.add(task)
            await con.commit()
        task_schema.task_id = task.task_id
        for question in task_request.dict()['questions']:
            await question_service.create_question(question['question_id'],question['question_type'],question['prompt'],
                                             question['resource'],question['options'] if question['question_type'] in ['single_choice','multi_choice'] else []
                                             ,task.task_id)
        await asyncio.shield(con.close())
        return task_schema

    async def claim_task(self,user_name,task_id)->schemas.tasks.Task | None:
        con = scoped_session(conection)
        async with con.begin():
            user = await con.execute(select(models.user.Respondent).where(models.user.Respondent.username == user_name).options(
                selectinload(models.user.Respondent.task_claimed)
            )
            )
            user = user.scalars().first()
            if user == None:
                await asyncio.shield(con.close())
                return None
            task = await con.execute(select(models.task.Task).where(models.task.Task.id==task_id).options(
                selectinload(models.task.Task.respondents_claimed)
            ))
            task = task.scalars().first()
            if task == None:
                await asyncio.shield(con.close())
                return None
            user.task_claimed.append(task)
            response_task = schemas.tasks.Task(task)
            await con.commit()
            await asyncio.shield(con.close())
            return response_task

    async def get_task(self, task_id: int) -> schemas.tasks.Task | str:
        con = scoped_session(conection)
        result = await con.execute(select(models.task.Task).where(models.task.Task.task_id == task_id).options(
            selectinload(models.task.Task.questions),
            selectinload(models.task.Task.respondents_claimed),
            selectinload(models.task.Task.respondents_complete),
        ))
        target = result.scalars().first()
        if target is None:
            await asyncio.shield(con.close())
            return None
        dict = target.dict()
        del dict['tags']
        dict['tags'] = set(target.tags.split('|'))
        del dict['questions']
        del dict['respondents_claimed']
        del dict['respondents_complete']
        dict['respondents_claimed'] =set(list(map(lambda A:A.username,target.respondents_claimed))) 
        dict['respondents_complete'] =set(list(map(lambda A:A.username,target.respondents_complete))) 

        response_task = schemas.tasks.Task(**dict)
        for question in target.questions:
            qtype = question.question_type
            di = question.dict()
            del di['id_in_task']
            del di['options']
            if di['resource'] == 'None':
                del di['resource']
            di['question_id'] = question.id_in_task
            if qtype == 'single_choice':
                di['options'] = question.options.split('|')
                q = schemas.questions.SingleChoiceQuestion(**di)
                answers = await con.execute(select(models.answer.SingleChoiceAnswer).where(models.answer.SingleChoiceAnswer.question_id==q.question_id))
                answers = answers.scalars().all()
                q.answers = list(map(lambda A:schemas.answers.SingleChoiceAnswer(choice = A.choice),answers))
            elif qtype == 'multi_choice':
                di['options'] = question.options.split('|')
                q = schemas.questions.MultiChoiceQuestion(**di)
                answers = await con.execute(select(models.answer.MultiChoiceAnswer).where(models.answer.MultiChoiceAnswer.question_id==q.question_id))
                answers = answers.scalars().all()
                q.answers = list(map(lambda A:schemas.answers.MultiChoiceAnswer(choices = A.choices),answers))
            elif qtype == 'bounding_box':
                q = schemas.questions.BoundingBoxQuestion(**di)
                answers = await con.execute(select(models.answer.BoundingBoxAnswer).where(models.answer.BoundingBoxAnswer.question_id==q.question_id))
                answers = answers.scalars().all()
                for target in answers:
                    p1 = schemas.answers.Point(x = target.top_left_x, y= target.top_left_y)
                    p2 = schemas.answers.Point(x = target.bottom_right_x, y= target.bottom_right_y)
                    q.answers.append(schemas.answers.BoundingBoxAnswer(top_left=p1,bottom_right=p2))
            elif qtype == 'open':
                q = schemas.questions.OpenQuestion(**di)
                answers = await con.execute(select(models.answer.OpenAnswer).where(models.answer.OpenAnswer.question_id==q.question_id))
                answers = answers.scalars().all()
                q.answers = list(map(lambda A:schemas.answers.OpenAnswer(text = A.text),answers))
            else : 
                continue
            response_task.questions.append(q)
        claim_names = list(map(lambda A:A.username,target.respondents_claimed))
        response_task.respondents_claimed = set(claim_names)
        complete_names = list(map(lambda A:A.username,target.respondents_complete))
        response_task.respondents_completed = set(complete_names)
        await asyncio.shield(con.close())
        return response_task

    
    async def delete_task(self,task_id:int) -> str | None:
        con = scoped_session(conection)
        async with con.begin():
            result = await con.execute(select(models.task.Task).where(models.task.Task.task_id==task_id))
            target = result.scalars().first()
            if target == None:
                return 'not_found'
            await con.delete(target)
            await con.commit()
            await asyncio.shield(con.close())

    async def claim_task(self,user_name,task_id)->schemas.tasks.Task | None:
        con = scoped_session(conection)
        async with con.begin():
            user = await con.execute(select(models.user.Respondent).where(models.user.Respondent.username == user_name).options(
                selectinload(models.user.Respondent.task_claimed)
            )
            )
            user = user.scalars().first()
            if user == None:
                await asyncio.shield(con.close())
                return None
            task = await con.execute(select(models.task.Task).where(models.task.Task.task_id==task_id).options(
                selectinload(models.task.Task.respondents_claimed),selectinload(models.task.Task.respondents_complete)
            ))
            task = task.scalars().first()
            if task == None:
                await asyncio.shield(con.close())
                return None
            user.task_claimed.append(task)
            info = {
                'task_id' :task_id,
                'requester': task.requester,
                'date_created':task.date_created,
                'resource_path':task.resource_path,
            }
            response_task = schemas.tasks.Task(**info)
            response_task.respondents_claimed =set(list( map(lambda A: A.username,task.respondents_claimed)))
            response_task.respondents_claimed.add(user_name)
            response_task.respondents_completed =set( list(map(lambda A: A.username,task.respondents_complete)))
            await con.commit()
            await asyncio.shield(con.close())
            return response_task
            
    async def process_task_archive(self, path: pathlib.Path) -> schemas.tasks.Task | str:
        '''
        Filename: filename of the file that was uploaded
        Creates and returns the task, or returns an error message
        '''
        con = scoped_session(conection)
        output_dir = path.parent / path.stem
        try:
            response = patoolib.extract_archive(str(path), outdir=output_dir, verbosity=-1, interactive=False)
        except Exception as e:
            return str(e)

        try:
            with open(output_dir / 'task.json', 'rb') as f:
                data = f.read()
        except FileNotFoundError:
            return '`task.json` not found'

        try:
            data = json.loads(data)
        except Exception as e:
            return str(e)


        try:
            questions = data['questions']
        except:
            return 'No questions'

        del data['questions']

        try:
            task = schemas.tasks.CreateTaskRequest.parse_obj(data)
        except Exception as e:
            return str(e)


        for question in questions:
            try:
                task.questions.append(schemas.questions.QUESTION_TYPES[question['question_type']].parse_obj(question))
            except Exception as e:
                return str(e)
        await asyncio.shield(con.close())
        return task

        


    async def search(self, 
        user: schemas.users.User,
        parameters = schemas.tasks.TaskSearchRequest
    ) -> tuple[list[schemas.tasks.Task], int]:
        """
Gets the tasks matching the search criteria\n
Returns: list of `Task`s matching the query within the specified `page` and `page_size`, and total number of `Task`s matching the query
        """


        # TODO: use query parameters from `parameters`


        con = scoped_session(conection)
        if parameters.sort_ascending is True:
            result = await con.execute(select(models.task.Task).where(and_(
                        or_ (parameters.name == '',models.task.Task.name == parameters.name),
                        or_ (parameters.credits_min == 0  , models.task.Task.credits >= parameters.credits_min),
                        or_ (parameters.credits_max == -1 , models.task.Task.credits <= parameters.credits_max),
                        )).order_by(models.task.Task.task_id.asc())
                        .options(selectinload(models.task.Task.questions),selectinload(models.task.Task.respondents_claimed),
                                 selectinload(models.task.Task.respondents_complete)))
                    
        else:           
            result = await con.execute(select(models.task.Task).where(and_(
                        or_ (parameters.name == '',models.task.Task.name == parameters.name),
                        or_ (parameters.credits_min == 0  , models.task.Task.credits >= parameters.credits_min),
                        or_ (parameters.credits_max == -1 , models.task.Task.credits <= parameters.credits_max),
                        )).order_by(models.task.Task.task_id.desc()) 
                        .options(selectinload(models.task.Task.questions),selectinload(models.task.Task.respondents_claimed),
                                 selectinload(models.task.Task.respondents_complete)))
                    
                        
        tasks = result.scalars().all()
        response_tasks = []
        if parameters.page_size == -1:
            for task in tasks :
                response_task = await task_service.get_task(task.task_id)
                response_tasks.append(response_task)
            await asyncio.shield(con.close())
            return response_tasks , len(tasks)
        else :
            if len(tasks) > parameters.page * parameters.page_size:
                target = tasks[(parameters.page-1)*parameters.page_size:parameters.page*parameters.page_size-1]
                for task in target :
                    response_task = await task_service.get_task(task.task_id)
                response_tasks.append(response_task)
                await asyncio.shield(con.close())
                return response_tasks , len(target)
            elif len(tasks) < (parameters.page-1)*parameters.page_size:
                await asyncio.shield(con.close())
                return [] , 0
            else :

                if len(tasks) > parameters.page * parameters.page_size:
                    target = tasks[(parameters.page-1)*parameters.page_size:parameters.page*parameters.page_size-1]
                    for task in target :
                        response_task = await task_service.get_task(task.task_id)
                        response_tasks.append(response_task)
                    await asyncio.shield(con.close())
                    return response_tasks, len(target)
                elif len(tasks) < (parameters.page-1)*parameters.page_size:
                    await asyncio.shield(con.close())
                    return [], 0
                else :
                    target = tasks[(parameters.page-1)*parameters.page_size:-1]
                    for task in target :
                        response_task = await task_service.get_task(task.task_id)
                        response_tasks.append(response_task)
                    await asyncio.shield(con.close())
                    return response_tasks, len(target)


    async def create_task_results_file(self, task_id: int) -> pathlib.Path | str:
        '''
        id: ID of the task
        Create the ZIP file containing the results of the task with ID `id`
        Returns the filename of the zip file as a pathlib.Path object if successful
        Returns a str detailing the error if it failed
        '''

        filename = 'results_' + str(task_id) + '_' + datetime_now_str() + '.zip'
        task = self.get_task(task_id)


        return filename


task_service = Tasks()




