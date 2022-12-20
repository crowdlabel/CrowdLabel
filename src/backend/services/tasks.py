from typing import Iterable
import schemas.questions
from utils.datetime_str import datetime_now_str
from datetime import datetime

from services.database import engine
import services.questions
import models.task
import models.user
from sqlalchemy.orm import sessionmaker, scoped_session, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_ ,or_
Connection = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
con = scoped_session(Connection)

import pathlib

import schemas.tasks
import schemas.users

import asyncio
import json
import patoolib
from utils.config import get_config
TASK_UPLOAD_DIR = pathlib.Path(get_config('file_locations.tasks'))

from services.users import user_service




class Tasks:

    def __init__(self):
        pass


    async def create_task(self,
        requester: schemas.users.Requester,
        task_request: schemas.tasks.CreateTaskRequest,
        resource_path: pathlib.Path    
    ) -> schemas.tasks.Task | str:

        if task_request.responses_required <= 0:
            return '`responses_required` must be positive'
        if task_request.credits < 0:
            return '`credits` must be positive'

        response = await user_service.handle_transaction(
            schemas.users.TransactionRequest(amount=task_request.credits * task_request.responses_required),
            user=requester
        )
        if not isinstance(response, float):
            return response

        # TODO: which task_id to use?

        task_schema = schemas.tasks.Task(**task_request.dict(), 
            task_id=1,
            requester=requester.username,
            date_created=datetime.utcnow(),
        )
        task = models.task.Task(**task_schema.dict(),
            resource_path=str(resource_path)
        )
        async with con.begin():
            target = await con.execute(select(models.user.Requester).where(models.user.Requester.username==requester.username).options(selectinload(models.user.Requester.task_requested)))
            res = target.scalars().first()
            if res == None:
                return 'requester not found'
        res.task_requested.append(task)
        con.add(task)
        await con.commit()

        return task_schema

    async def claim_task(self,user_name,task_id)->schemas.tasks.Task | None:
        async with con.begin():
            user = await con.execute(select(models.user.Respondent).where(models.user.Respondent.username == user_name).options(
                selectinload(models.user.Respondent.task_claimed)
            )
            )
            user = user.scalars().first()
            if user == None:
                return None
            task = await con.execute(select(models.task.Task).where(models.task.Task.id==task_id).options(
                selectinload(models.task.Task.respondent_claimed)
            ))
            task = task.scalars().first()
            if task == None:
                return None
            user.task_claimed.append(task)
            response_task = schemas.tasks.Task(task)
            return response_task

    async def get_task(self, task_id: int) -> schemas.tasks.Task | None:
        async with con.begin():
            result = await con.execute(select(models.task.Task).where(models.task.Task.id == task_id).options(
                selectinload(models.task.Task.questions),
                selectinload(models.task.Task.respondent_claimed),
                selectinload(models.task.Task.respondent_complete)
            ))
            target = result.scalars().first()
            if target is None:
                return None
            response_task = schemas.tasks.Task(target)
            for question in target.questions:
                qtype = question.question_type
                if qtype == 'single_choice':
                    q = schemas.questions.SingleChoiceQuestion(question)
                elif qtype == 'multi_choice':
                    q = schemas.questions.MultiChoiceQuestion(question)
                elif qtype == 'ranking':
                    q = schemas.questions.RankingQuestion(question)
                elif qtype == 'open':
                    q = schemas.questions.OpenQuestion(question)
                else : 
                    continue
                response_task.questions.append(q)
            claim_names = list(map(lambda A:A.username,target.respondent_claimed))
            response_task.respondents_claimed = set(claim_names)
            complete_names = list(map(lambda A:A.username,target.respondent_complete))
            response_task.respondents_completed = set(complete_names)
            return response_task

    
    async def delete_task(task_id:int) -> bool:
        async with con.begin():
            result = await con.execute(select(models.task.Task).where(models.task.Task.id==task_id))
            target = result.scalars().first()
            if target == None:
                return False
            await con.delete(target)
            # for item in result:
            #     await con.delete(item)
        await con.commit()
        return True

    async def claim_task(self, task: schemas.tasks.Task | int, respondent: schemas.users.Respondent) -> str | None:
        if isinstance(task, int):
            task = await self.get_task(task)
        if not isinstance(task, schemas.tasks.Task):
            return task
        respondent.tasks_claimed.add(task.task_id)
        task.respondents_claimed.add(respondent.username)
        # TODO: claim task in database
        return None
        # returns error message, or none if successful
            
    async def process_task_archive(self, path: pathlib.Path) -> schemas.tasks.Task | str:
        '''
        Filename: filename of the file that was uploaded
        Creates and returns the task, or returns an error message
        '''
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

        return task

        


    async def search(
        user: schemas.users.User,
        parameters = schemas.tasks.TaskSearchRequest
    ) -> tuple[list[schemas.tasks.Task], int]:

        """
        Gets the tasks matching the search criteria

        Parameters:
            `username`: username of the querier
            `name`: name of the task
            `tags`: Iterable of tags
            `creator`: username of the person who created the task
            `credits`: number of credits rewarded upon task completion
            `questions_min`: minimum number of questions in the task
            `questions_max`: maximum number of questions in the task
            `page`: the page
            `page_size`: the size of each page; if -1 then `page` would not be considered and all results will be returned
                e.g., if `page` is 2 and `page_size` is 10, then it will return the 11th to 20th results, inclusive
                e.g., if `page` is _ and `page_size` is -1, then it will return all the results
            `sort_criteria`: criteria that the results should be sorted against
            `sort_ascending`: True to sort in ascending order, False to sort in descending order


        Returns: list of Tasks queried, and total number of tasks

        """

        # TODO: creator -> requesters, multiple usernames

        async with con.begin():

            result = await con.execute(select(models.task.Task))

            '''
            if sort_ascending is True:
                result = await con.execute(select(models.task.Task).where(and_(
                            or_(models.task.Task.name == name, name ==None),
                            models.task.Task.credits >= credits_min,
                            models.task.Task.credits <= credits_max,
                            len(models.task.Task.questions)>questions_min,
                            len(models.task.Task.questions)<questions_max,),
                            or_(models.task.Task.response_required == result_count , result_count == -1))
                            .order_by(models.task.Task.id.asc()).options(selectinload(models.task.Task.questions),selectinload(models.task.Task.results)))
            else:
 
                result = await con.execute(select(models.task.Task).where(and_(
                                or_(models.task.Task.name == name, name ==None),
                                models.task.Task.credits >= credits_min,
                                models.task.Task.credits <= credits_max,
                                len(models.task.Task.questions)>questions_min,
                                len(models.task.Task.questions)<questions_max,),
                                or_(models.task.Task.response_required == result_count , result_count == -1))
                                .order_by(models.task.Task.id.desc()).options(selectinload(models.task.Task.questions),selectinload(models.task.Task.results)))
            '''

            tasks = result.scalar().all()
            if parameters.page_size == -1:
                return tasks , len(tasks)
            else :
                if len(tasks) > parameters.page * parameters.page_size:
                    target = tasks[(parameters.page-1)*parameters.page_size:parameters.page*parameters.page_size-1]
                    return target , len(target)
                elif len(tasks) < (parameters.page-1)*parameters.page_size:
                    return [] , 0
                else :
                    target = tasks[(parameters.page-1)*parameters.page_size:-1]
                    return target ,len(target)

    async def create_task_results_file(self, id: int) -> str:
        '''
        id: ID of the task
        Create the ZIP file containing the results of the task with ID `id`
        Returns the filename of the zip file
        '''

        filename = 'results_' + id + '_' + datetime_now_str() + '.zip'



        return filename


task_service = Tasks()




