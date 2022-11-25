from models.results import Results
from sqlalchemy.orm import sessionmaker, scoped_session, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select ,update
from .database import *
Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)
def __verify_result_format():
    return True


    

async def create_result(
    name: str,
    creator: str,
    details: str
):

    # get the arguments as a dictionary
    if not __verify_result_format():
        return False


    result = Results(
        name,
        creator,
        details
    )
    con.add(result)
    await con.commit()
    print(123)
    return {
        'arg': 'ok',
        'error': 'ok',
    }

async def get_result(id):
    async with con.begin():
        result = await con.execute(select(Results).where(Results.id==id))#.options(selectinload(Task.questions)))
        target = result.scalars().first()
        if target is None:
            return{
                "status":"not found",
            },400
        s= ''
        for q in target.questions:
            print(q.prompt)
            s = s+q.prompt+'\n'

    return {
        "status":"ok",
        "id" :target.id,
        "name":target.name,
        "creator":target.creator,
        "details":target.details,
        "questions":s
    },200

async def edit_result(id,details):
    async with con.begin():
        result = await con.execute(select(Results).where(Results.id==id))
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
    

async def delete_result(id):
    async with con.begin():
        result = await con.execute(select(Results).where(Results.id==id))
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