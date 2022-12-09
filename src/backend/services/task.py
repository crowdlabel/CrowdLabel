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


    

async def create_task(
    name: str,
    creator: str,
    type:int,
    details:str,
    introduction: str,
    path:str
):

    # get the arguments as a dictionary
    if not __verify_task_format():
        return {
            'status':'error'
        }


    task = Task(
        name,
        creator,
        details,
        introduction,
        type,
        path
    )
    con.add(task)
    await con.commit()
    return {
        'status':'ok'
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
        "status":"ok",
        "id" :target.id,
        "name":target.name,
        "creator":target.creator,
        "introduction":target.introduction,
        "type":target.type,
        "details":target.details,
        "questions":s,
        "results":result,
        "path":target.path   
    },200
async def edit_task(id,details,introduction):
    async with con.begin():
        result = await con.execute(select(Task).where(Task.id==id))
        target = result.scalars().first()
        if target is None:
            return{
                "status":"not found",
            },400
        target.details= details
        target.introduction = introduction
        await con.flush()
        con.expunge(target)
    return {
        "status":"ok",
        "id" :target.id,
        "name":target.name,
        "creator":target.creator,
        "introduction":target.introduction,
        "type":target.type,
        "details":target.details
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