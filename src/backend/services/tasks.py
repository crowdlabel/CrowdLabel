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

import schemas.tasks
import schemas.users

import asyncio
import zipfile
import rarfile
import json
class Tasks:

    def __init__(self):
        pass

    async def create_task(self, creator: schemas.users.Requester, name: str, description: str,
                          introduction: str, tags: set[str], cover_path: str, responses_required: int,
                          credits: float) -> schemas.tasks.Task | str:

        if responses_required < 1:
            return '`responses_required` must be positive'
        if credits < 0:
            return '`credits` must be positive'
        if credits * responses_required > creator.credits:
            return 'Insufficient credits'

        date_created = datetime.datetime.utcnow()
        task_schema = schemas.tasks.Task(
            name=name,
            credits=credits,
            introduction=introduction,
            description=description,
            tags=tags,
            responses_required=responses_required,
            date_created=date_created,
        )

        # if not __verify_task_format():
        #     return None
        filepath = 0 # TODO
        task = models.task.Task(creator = creator.username , name = name ,description = description ,
                    introduction = introduction ,cover_path = cover_path ,
                    response_required = responses_required,credits = credits,date_created = date_created,filepath = filepath)
                    
        async with con.begin():
            target = await con.execute(select(models.user.Requester).where(models.user.Requester.username==creator.username).options(selectinload(models.user.Requester.task_requested)))
            res = target.scalars().first()
            if res == None:
                return 'requester not found'
        res.task_requested.append(task)
        con.add(task)
        await con.commit()
        response_task = schemas.tasks.Task()
        response_task.cover = cover_path
        response_task.creator=creator.username
        response_task.credits=credits
        response_task.date_created=date_created
        response_task.description=description
        response_task.introduction=introduction
        response_task.name=name
        response_task.tags = []
        response_task.task_id = task.id
        response_task.responses_required = responses_required
        questions = self.process_task_archive(task.id,filepath)
        response_task.questions = questions
        return response_task

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
            
    async def process_task_archive(self,task_id,filename: str) -> list[schemas.questions.Question] | str:
        '''
        Filename: filename of the file that was uploaded
        Creates and returns the task, or returns an error message
        '''
        suffix = filename.split('.')[-1]
        if suffix == 'zip':
            file = zipfile.ZipFile(filename)
        elif suffix == 'rar':  
            file = rarfile.RarFile(filename)
        file.extractall()
        questions = services.questions.question_service.create_question_from_file(task_id,'questions.json')
        return questions

    async def search(
        user: schemas.users.User,
        name: str=None,
        tags: Iterable=None,
        credits_min: float=0,
        credits_max: float=None,
        questions_min: int=0,
        questions_max: int=10e9,
        requesters: set[str]=None,
        result_count: int=-1,
        page: int=1,
        page_size: int = -1,
        sort_criteria: str=None,
        sort_ascending: bool=True,
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
            if page_size == -1:
                return tasks , len(tasks)
            else :
                if len(tasks) > page*page_size:
                    target = tasks[(page-1)*page_size:page*page_size-1]
                    return target , len(target)
                elif len(tasks) < (page-1)*page_size:
                    return [] , 0
                else :
                    target = tasks[(page-1)*page_size:-1]
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




