from models.child_results import ChildResults
from sqlalchemy.orm import sessionmaker, scoped_session, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select ,update
from .database import *
import datetime
Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)
def __verify_result_format():
    return True


async def create_result(
    response: str,
    id:int 
):

    # get the arguments as a dictionary
    if not __verify_result_format():
        return {
            'status':'error'
        },400


    result = ChildResults(
        response,id
    )
    con.add(result)
    await con.commit()
    return {
        'status':'ok',
        'arg': 'ok',
        'error': 'ok',
    },200   

async def get_result(id):
    async with con.begin():
        result = await con.execute(select(ChildResults).where(ChildResults.id==id)) #.options(selectinload(Task.questions)))
        target = result.scalars().first()
        print(target.result_id)
        if target is None:
            return{
                "status":"not found",
            },400
    return {
        "status":"ok",
        "id" :target.id,
        "result_id":target.result_id,
        "response":target.response,
    },200

async def edit_result(id,response):
    async with con.begin():
        result = await con.execute(select(ChildResults).where(ChildResults.id==id))
        target = result.scalars().first()
        if target is None:
            return{
                "status":"not found",
            },400
        target.response = response
        await con.flush()
        con.expunge(target)
    return {
        "status":"ok",
        "id" :target.id,
        "result_id":target.result_id,
        "response":target.response,
    },200
    

async def delete_result(id):
    async with con.begin():
        result = await con.execute(select(ChildResults).where(ChildResults.id==id))
        target = result.scalars().first()
        if target == None:
            return {
                "status": 'not found'
            },400
        await con.delete(target)

    await con.commit()
    return {
        'status':'ok'
    },200