from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from models.basicbase import Base
from models.child_results import ChildResults
from models.email import Email
from models.question import Question
from models.results import Results
from models.task import Task
from models.user import User
import asyncio
#from utils.config import get_config

db_params = f"sqlite+aiosqlite:///crowdlabel.db"

engine = create_async_engine(db_params)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(init_models())

