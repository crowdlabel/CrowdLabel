from models.results import Results
from sqlalchemy.orm import sessionmaker, scoped_session, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select ,update
from .database import *
from datetime import datetime
Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)
def __verify_result_format():
    return True


    

async def create_result(
    name: str,
    id:int 
):

    # get the arguments as a dictionary
    if not __verify_result_format():
        return {
            'status':'error'
        },400


    result = Results(
        id,name
    )
    con.add(result)
    await con.commit()
    return {
        'status':'ok',
        'arg': 'ok',
        'error': 'ok',
         },200   

# async def get_result(id):
#     async with con.begin():
#         result = await con.execute(select(Results).where(Results.id==id).options(selectinload(Results.child_result)))
#         target = result.scalars().first()
#         info = ""
#         for child in target.child_result:
#             info = info + str(child.id) + '\n'
#             info = info + child.response + '\n'
#         if target is None:
#             return{
#                 "status":"not found",
#             },400
#     return {
#         "status":"ok",
#         "id" :target.id,
#         "name":target.name,
#         "task_id":target.task_id,
#         "date_created":target.date_created,
#         "date_download":target.date_download,
#         "info":info
#     },200


async def edit_result(id):
    async with con.begin():
        result = await con.execute(select(Results).where(Results.id==id))
        target = result.scalars().first()
        if target is None:
            return{
                "status":"not found",
            },400
        target.date_download=datetime.utcnow()
        await con.flush()
        con.expunge(target)
    return {
        "status":"ok",
        "id" :id,
        "name":target.name,
        "task_id":target.task_id,
        "date_created":target.date_created,
        "date_download":target.date_download
    },200

    

# async def delete_result(id):
#     async with con.begin():
#         result = await con.execute(select(Results).where(Results.id==id))
#         target = result.scalars().first()
#         if target == None:
#             return {
#                 "status": 'not found'
#             },400
#         await con.delete(target)
#         # for item in result:
#         #     await con.delete(item)
#     await con.commit()
#     return {
#         'status':'ok'
#     },200