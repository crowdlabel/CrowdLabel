from models.task import Task
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
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
    con.commit()

    return {
        'arg': 'ok',
        'error': 'ok',
    }

def get_task(id):
    pass

def edit_task(id):
    pass

def delete_task(id):
    pass
