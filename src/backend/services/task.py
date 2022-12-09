from models.task import Task
from sqlalchemy.orm import sessionmaker, scoped_session, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select ,update
from .database import *
import datetime
Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)
def __verify_task_format():
    return True

from typing import Iterable
    

async def create_task(
    name: str,
    creator: str,
    details: str
):

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

async def get_task(id):
    async with con.begin():
        result = await con.execute(select(Task).where(Task.id==id).options(selectinload(Task.questions),selectinload(Task.results)))
        target = result.scalars().first()
        if target is None:
            return{
                "status":"not found",
            },400
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
    }, 200


async def get_tasks(
    username: str,
    name: str=None,
    tags: Iterable=None,
    reward: float=None,
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
        `reward`: number of tokens rewarded upon task completion
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

async def edit_task(id):
    async with con.begin():
        result = await con.execute(select(Task).where(Task.id==id))
        target = result.scalars().first()
        if target is None:
            return{
                "status":"not found",
            },400
        target.date_download = datetime.datetime.now
        await con.flush()
        con.expunge(target)
    return {
        "status":"ok",
        "id" :target.id,
        "task_name":target.task_name,
        "task_id":target.task_id,
        "date_create":target.date_created,
        "date_download":target.date_download
    },200
    

async def delete_task(id):
    async with con.begin():
        result = await con.execute(select(Task).where(Task.id==id))
        target = result.scalars().first()
        if target == None:
            return {
                "status": 'not found'
            },400
        await con.delete(target)
        # for item in result:
        #     await con.delete(item)
    await con.commit()
    return {
        'status':'ok'
    },200


async def create_task_results_file(id):

    """
    Create the ZIP file containing the results of the task with ID `id
    """


    
    pass