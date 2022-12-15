from typing import Optional, Iterable
from pydantic import BaseModel
import schemas.questions
from services.users import User
from utils.datetime_str import datetime_now_str
from datetime import datetime

from services.database import *
from models.task import Task
from sqlalchemy.orm import sessionmaker, scoped_session, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update ,and_ ,or_
Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)
def __verify_task_format():
    return True




from datetime import datetime

class Task(BaseModel):
    task_id: int
    creator: str
    date_created: datetime
    credits: float
    name: str
    introduction: str=''
    description: str=''
    cover: str=''
    tags: list[str]=[]
    responses_required: int
    respondents_claimed: set[str]=set() # usernames of respondents who have claimed the task but have not completed it
    respondents_completed: set[str]=set() # usernames of respondents who have claimed and completed the task
    questions: list[schemas.questions.Question]=[] # list of Questions



    async def create_task_results_file(id: int) -> str:
        '''
        id: ID of the task
        Create the ZIP file containing the results of the task with ID `id`
        Returns the filename of the zip file
        '''

        filename = 'results_' + id + '_' + datetime_now_str() + '.zip'



        return filename
        


fake_tasks = [
    Task(
        task_id=1,
        name='faketask',
        creator='requester1',
        responses_required=10,
        date_created=datetime.utcnow(),
        credits=10,
        questions=[
            schemas.questions.SingleChoiceQuestion(
                task_id=1,
                question_id=1,
                prompt='Which number is a prime number?',
                options=['9', '10', '11', '12'],
                answers=[],
            ),
        ]
    ),
]

NO_DB = True


class Tasks:

    def __init__(self):
        pass

    async def create_task(self,creator: str ,name:str ,description:str,
                          introduction:str,cover_path:str,response_required:int,
                          credits:int) -> Task | None:
        date_created = datetime.utcnow()
        # if not __verify_task_format():
        #     return None
        task = Task(creator = creator , name = name ,description = description ,
                    introduction = introduction ,cover_path = cover_path ,
                    response_required = response_required,credits = credits,date_created = date_created)
        con.add(task)
        await con.commit()
        return task


    async def get_task(self, task_id: int) -> Task | None:

        for task in fake_tasks:
            if task.task_id == task_id:
                return task

        return None

        async with con.begin():
            result = await con.execute(select(Task).where(Task.id == task_id).options(selectinload(Task.questions),
                                                                                      selectinload(Task.results),
                                                                                      selectinload(Task.requester),
                                                                                      selectinload(Task.respondent_claimed),
                                                                                      selectinload(Task.respondent_complete)))
            target = result.scalars().first()
            if target is None:
                return None
            return target
    async def delete_task(task_id:int) -> bool:
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
            
    async def process_task_archive(self, filename: str) -> Task | str:
        '''
        Filename: filename of the file that was uploaded
        Creates and returns the task, or returns an error message
        '''
        pass



    async def search(
        user: User,
        name: str=None,
        tags: Iterable=None,
        credits_min: float=None,
        credits_max: float=None,
        questions_min: int=-1,
        questions_max: int=10e9,
        requesters: set[str]=None,
        result_count: int=-1,
        page: int=1,
        page_size: int = -1,
        sort_criteria: str=None,
        sort_ascending: bool=True,
    ) -> tuple[list[Task], int]:

        tasks = []
        total = 0

        return fake_tasks, len(fake_tasks)

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
        async with con.begin():
            if sort_ascending is True:
                result = await con.execute(select(Task).where(and_(or_(Task.creator == creator,creator == None),
                                                                or_(Task.name == name, name ==None),
                                                                or_(Task.credits == credits,credits = None),
                                                                len(Task.questions)>questions_min,
                                                                len(Task.questions)<questions_max,),
                                                                or_(Task.response_required == result_count , result_count == -1))
                                                                .order_by(Task.id.asc()).options(selectinload(Task.questions),selectinload(Task.results)))
            else:
 
                result = await con.execute(select(Task).where(and_(or_(Task.creator == creator,creator == None),
                                                                or_(Task.name == name, name ==None),
                                                                or_(Task.credits == credits,credits = None),
                                                                len(Task.questions)>questions_min,
                                                                len(Task.questions)<questions_max,),
                                                                or_(Task.response_required == result_count , result_count == -1))
                                                                .order_by(Task.id.desc()).options(selectinload(Task.questions),selectinload(Task.results)))
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
if __name__ == '__main__':
    t = Tasks()
    asyncio.run(asyncio.wait([t.create_task('chenjz20','tsk1','des','intro','./1.png',10,10)]))