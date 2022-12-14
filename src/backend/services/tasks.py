import datetime
from sqlalchemy.orm import sessionmaker, scoped_session, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from models.task import Task
from .database import *
from .fakedata import fake_tasks

from pydantic import BaseModel
import pathlib

Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)
def __verify_task_format():
    return True

from typing import Iterable


class Tasks:

    def __init__(self):
        pass

    async def process_task_archive(self, filename: str):
        pass

    async def create_task(self, 
        name: str,
        creator: str,
        details: str
    ) -> Task:

        # get the arguments as a dictionary
        if not __verify_task_format():
            return False


        task = Task(
            name,
            creator,
            details
        )
        con.add(task)
        await con.commit()
        print(123)
        return {
            'arg': 'ok',
            'error': 'ok',
        }

    async def get_task(task_id: int) -> dict | None:

        for task in fake_tasks:
            if task.task_id == task_id:
                return task
        return None

        async with con.begin():
            result = await con.execute(select(Task).where(Task.id == task_id).options(selectinload(Task.questions),selectinload(Task.results)))
            target = result.scalars().first()
            if target is None:
                return None
            s= ''
            for q in target.questions:
                s = s+q.prompt+'\n'
            result = ''
            for r in target.results:
                result = result+str(r.date_created)+'\n'
        return {
            "status": "ok",
            "id" : target.id,
            "name": target.name,
            "creator": target.creator,
            "details": target.details,
            "questions": s,
            "results": result    
        }


    async def get_tasks(
        username: str,
        name: str=None,
        tags: Iterable=None,
        credits: float=None,
        questions_min: int=1,
        questions_max: int=-1,
        creator: str=None,
        result_count: int=-1,
        page: int=1,
        sort_criteria: str=None,
        sort_ascending: bool=True,
    ):
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
        total = 10
        return [], total


class Task(BaseModel):
    task_id: int
    creator: str
    date_created: datetime
    credits: float
    name: str
    introduction: str=''
    description: str=''
    cover: pathlib.Path=None
    tags: set[str]={}
    responses_required: int
    respondents_claimed: set[str]={} # usernames of respondents who have claimed the task but have not completed it
    respondents_completed: set[str]={} # usernames of respondents who have claimed and completed the task
    questions: list[Question] # list of Questions

    def set_id(self, new_id):
        self.task_id = new_id
    def __init__(self):
        pass
    async def edit_task(task_id: int) -> bool | None:
        async with con.begin():
            result = await con.execute(select(Task).where(Task.id == task_id))
            target = result.scalars().first()
            if target is None:
                return None
            target.date_download = datetime.datetime.now()
            await con.flush()
            con.expunge(target)

        return {
            "id" :target.id,
            "task_name":target.task_name,
            "task_id":target.task_id,
            "date_create":target.date_created,
            "date_download":target.date_download
        }
        

    async def delete(self, task_id: int) -> bool:
        async with con.begin():
            result = await con.execute(select(Task).where(Task.id==task_id))
            target = result.scalars().first()
            if target == None:
                return False
            await con.delete(target)
            # for item in result:
            #     await con.delete(item)
        await con.commit()
        return True


    async def create_task_results_file(id):

        """
        Create the ZIP file containing the results of the task with ID `id
        """

        return 'main.py'
        
        pass