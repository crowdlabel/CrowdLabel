from models.question import Question
from models.task import Task
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select ,update
from .database import *
import json
Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)
def __verify_question_format():
    return True


async def create_question_from_file(
    task_id:int,
    file_path:str
):
    if not __verify_question_format():
        return False
    file = json.load(open(file_path,'r'))
    async with con.begin():
        result = await con.execute(select(Task).where(Task.id==task_id))
        target = result.scalars().first()
        type = target.type
    for question in file:
        await create_question(type,file[question]['prompt'],file_path,file[question]['options'],task_id)
    return {
        'status':'ok'
    }

async def create_question(
    type: str,
    prompt:str,
    resource:str,
    options:str,
    task_id
):

    # get the arguments as a dictionary
    if not __verify_question_format():
        return False

    question = Question(
        type,prompt,resource,options,task_id
    )
    con.add(question)
    await con.commit()
    return {
        'status':'ok'
    }

async def get_question(id):
    async with con.begin():
        result = await con.execute(select(Question).where(Question.id==id))
        target = result.scalars().first()
        if target is None:
            return{
                "status":"not found",
            },400
    return {
        "status":"ok",
        "type" :target.type,
        "prompt":target.prompt,
        "resource":target.resource,
        "options":target.options,
        "task_id":target.task_id
    },200

async def edit_question(id,type,prompt,resource,options,task_id):
    async with con.begin():
        result = await con.execute(select(Question).where(Question.id==id))
        target = result.scalars().first()
        if target is None:
            return{
                "status":"not found",
            },400
        target.type= type
        target.prompt =prompt
        target.resource = resource
        target.options = options
        target.task_id = task_id
        await con.flush()
        con.expunge(target)
    return {
        "status":"ok",
        "type" :target.type,
        "prompt":target.prompt,
        "resource":target.resource,
        "options":target.options,
        "task_id":target.task_id
    },200
    

async def delete_question(id):
    async with con.begin():
        result = await con.execute(select(Question).where(Question.id==id))
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