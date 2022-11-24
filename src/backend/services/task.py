from models.task import Task
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select ,update
from .database import *
Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)
def __verify_task_format():
    return True


    

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
    pass

async def edit_task(id,details):
    async with con.begin():
        result = await con.execute(select(Task).where(Task.id==id))
        target = result.scalars().first()
        if target is None:
            return{
                "status":"not found",
            },400
        target.details= details
        await con.flush()
        con.expunge(target)
    return {
        "status":"ok",
        "id" :target.id,
        "name":target.name,
        "creator":target.creator,
        "details":target.details
    }
    

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