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
import utils.config
TASK_UPLOAD_DIR = pathlib.Path(utils.config.config['directories']['tasks'])

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
            await asyncio.shield(con.close())
            return '`responses_required` must be positive'
        if task_request.credits <= 0:
            await asyncio.shield(con.close())
            return '`credits` must be positive'

        



        info = task_request.dict()
        del info['questions']
        task_schema = schemas.tasks.Task(**info, 
            task_id= 0,
            requester=requester.username,
            date_created=datetime.utcnow(),
            resource_path=resource_path
        )

        types = ['文字分类','图片分类','图片打标','音频分类']
        task_type = None
        for tag in task_request.tags:
            if tag in types:
                task_type = tag
        if task_type == None:
            await asyncio.shield(con.close())
            return 'Task without type'
        if task_type == '图片打标':
            for question in task_request.questions:
                if not isinstance(question,schemas.questions.BoundingBoxQuestion):
                    await asyncio.shield(con.close())
                    return 'Wrong question type'
                task_schema.questions.append(question)
        else:
            for question in task_request.questions:
                if isinstance(question,schemas.questions.BoundingBoxQuestion):
                    await asyncio.shield(con.close())
                    return 'Wrong question type'
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
        
        response = await user_service.handle_transaction(
            schemas.users.TransactionRequest(amount=- task_request.credits * task_request.responses_required),
            user=requester
        )
        if not isinstance(response, float):
            await asyncio.shield(con.close())
            return response
        
        async with con.begin():
            target = await con.execute(select(models.user.Requester)
                .where(models.user.Requester.username==requester.username).options(selectinload(models.user.Requester.task_requested)))
            res = target.scalars().first()
            if res == None:
                await asyncio.shield(con.close())
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
                answers = await con.execute(select(models.answer.SingleChoiceAnswer).where(models.answer.SingleChoiceAnswer.question_id==question.id))
                answers = answers.scalars().all()
                q.answers = list(map(lambda A:schemas.answers.Answer(date_created=A.date_answered,
                                                                     respondent=A.respondent_name,
                                                                     answer = schemas.answers.SingleChoiceAnswer(choice =A.choice)),
                                                                     answers))
            elif qtype == 'multi_choice':
                di['options'] = question.options.split('|')
                q = schemas.questions.MultiChoiceQuestion(**di)
                answers = await con.execute(select(models.answer.MultiChoiceAnswer).where(models.answer.MultiChoiceAnswer.question_id==question.id))
                answers = answers.scalars().all()
                q.answers = list(map(lambda A:schemas.answers.Answer(date_created=A.date_answered,
                                                                     respondent=A.respondent_name,
                                                                     answer = schemas.answers.MultiChoiceAnswer(choices = [] if A.choices == '' else [int(choice) for choice in A.choices.split('|')])),
                                                                     answers))
            elif qtype == 'bounding_box':
                q = schemas.questions.BoundingBoxQuestion(**di)
                answers = await con.execute(select(models.answer.BoundingBoxAnswer).where(models.answer.BoundingBoxAnswer.question_id==question.id).options(selectinload(models.answer.BoundingBoxAnswer.corner)))
                answers = answers.scalars().all()
                for single in answers:
                    boxes = []
                    for box in single.corner:
                        p1 = schemas.answers.Point(x = box.top_left_x, y= box.top_left_y)
                        p2 = schemas.answers.Point(x = box.bottom_right_x, y= box.bottom_right_y)
                        boxes.append(schemas.answers.Corners(top_left=p1,bottom_right=p2))
                    q.answers.append(schemas.answers.Answer(date_created=single.date_answered,
                                                            respondent=single.respondent_name,
                                                            answer = schemas.answers.BoundingBoxAnswer(boxes = boxes)))
            elif qtype == 'open':
                q = schemas.questions.OpenQuestion(**di)
                answers = await con.execute(select(models.answer.OpenAnswer).where(models.answer.OpenAnswer.question_id==question.id))
                answers = answers.scalars().all()
                q.answers = list(map(lambda A:schemas.answers.Answer(date_created=A.date_answered,
                                                                     respondent=A.respondent_name,
                                                                     answer = schemas.answers.OpenAnswer(text = A.text)),
                                                                     answers))
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
            result = await con.execute(select(models.task.Task).where(models.task.Task.task_id==task_id).options(selectinload(models.task.Task.respondents_claimed),selectinload(models.task.Task.respondents_complete)))
            target = result.scalars().first()
            if target == None:
                await asyncio.shield(con.close())
                return 'not_found'
            target.respondents_claimed = []
            target.respondents_complete = []
            await con.delete(target)
            await con.commit()
            await asyncio.shield(con.close())

    async def claim_task(self,user_name,task_id)->schemas.tasks.Task | str:
        """
        Returns a `Task` if the claim was successful, otherwise `str` describing the error
        """
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
            if len(task.respondents_complete) >= task.responses_required:
                await asyncio.shield(con.close())
                return 'Enough respondents have claimed this task'
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
            if parameters.sort_criteria == '' or parameters.sort_criteria == 'date':
                result = await con.execute(select(models.task.Task).where(and_(
                            or_ (parameters.credits_min == 0  , models.task.Task.credits >= parameters.credits_min),
                            or_ (parameters.credits_max == -1 , models.task.Task.credits <= parameters.credits_max),
                            )).order_by(models.task.Task.date_created.asc())
                            .options(selectinload(models.task.Task.questions),selectinload(models.task.Task.respondents_claimed),
                                    selectinload(models.task.Task.respondents_complete)))
            else:
                result = await con.execute(select(models.task.Task).where(and_(
                            or_ (parameters.credits_min == 0  , models.task.Task.credits >= parameters.credits_min),
                            or_ (parameters.credits_max == -1 , models.task.Task.credits <= parameters.credits_max),
                            )).order_by(models.task.Task.credits.asc())
                            .options(selectinload(models.task.Task.questions),selectinload(models.task.Task.respondents_claimed),
                                    selectinload(models.task.Task.respondents_complete)))
                    
        else:           
            if parameters.sort_criteria == '' or parameters.sort_criteria == 'date':
                result = await con.execute(select(models.task.Task).where(and_(
                            or_ (parameters.credits_min == 0  , models.task.Task.credits >= parameters.credits_min),
                            or_ (parameters.credits_max == -1 , models.task.Task.credits <= parameters.credits_max),
                            )).order_by(models.task.Task.date_created.desc())
                            .options(selectinload(models.task.Task.questions),selectinload(models.task.Task.respondents_claimed),
                                    selectinload(models.task.Task.respondents_complete)))
            else:
                result = await con.execute(select(models.task.Task).where(and_(
                            or_ (parameters.credits_min == 0  , models.task.Task.credits >= parameters.credits_min),
                            or_ (parameters.credits_max == -1 , models.task.Task.credits <= parameters.credits_max),
                            )).order_by(models.task.Task.credits.desc())
                            .options(selectinload(models.task.Task.questions),selectinload(models.task.Task.respondents_claimed),
                                    selectinload(models.task.Task.respondents_complete)))
                    
                        
        old_tasks = result.scalars().all()
        tasks = []
        for task in old_tasks:
            if (parameters.name == '' or parameters.name.lower() in task.name.lower() ) and (len(parameters.tags) == 0 or list(parameters.tags)[0] in task.tags.split('|')) and (len(parameters.requesters)==0 or list(parameters.requesters)[0] == task.requester):
                if parameters.respondent == '':
                        tasks.append(task)
                else:
                    for resp in task.respondents_complete:
                        if resp.username == parameters.respondent:
                            tasks.append(task)
                            break
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
        
        filename = 'results_' + str(task_id) + '_' + datetime_now_str() + '.json'
        path = TASK_UPLOAD_DIR / filename
        task = await self.get_task(task_id)
        task_dict = json.loads(task.json(exclude={'resource_path'}))
        with open(path, 'w', encoding='utf8') as f:
            json.dump(task_dict, f, ensure_ascii=False, indent=4) 
        return path

    async def complete(self, task_id: int, username: str) -> None | str:
        # TODO:
        # 0. check that the user `username` has answered all the questions in task `task_id`
        # 1. move username from tasks.respondents_claimed to tasks.respondents_compelted
        # 2. move task_id from user.tasks_claimed to user.tasks_completed
        # 3. Add credits to user
        # Returns `None` if no error occurred, or `str` which describes the error
        con = scoped_session(conection)
        res = await con.execute(select(models.task.Task).where(models.task.Task.task_id == task_id).options(
              selectinload(models.task.Task.questions),selectinload(models.task.Task.respondents_claimed),selectinload(models.task.Task.respondents_complete)))
        task = res.scalars().first()
        if task == None:
            await asyncio.shield(con.close())
            return 'task not found'
        for question in task.questions:
            res = await con.execute(select(models.answer.Answer).where(and_(models.answer.Answer.question_id == question.id,models.answer.Answer.respondent_name == username)))
            answer = res.scalars().first()
            if answer == None:
                await asyncio.shield(con.close())
                return f'answer not complete'


        res = await con.execute(select(models.user.Respondent).where(models.user.Respondent.username == username ))
        user = res.scalars().first()
        user.credits += task.credits
        task.respondents_complete.append(user)
        task.respondents_claimed.remove(user)
        await con.flush() 
        con.expunge(user)
        con.expunge(task)
        await con.commit()
        await asyncio.shield(con.close())
        return None

    async def remove_answers(self, user, task) -> schemas.tasks.Task:
        if user.username in task.respondents_claimed:
            for i in range(len(task.questions)):
                answers = []
                for answer in task.questions[i].answers:
                    if answer.respondent == user.username:
                        answers = [answer]
                        break
                task.questions[i].answers = answers
        elif user.user_type == 'respondent':
            for i in range(len(task.questions)):
                task.questions[i].answers = []
        

        

task_service = Tasks()




