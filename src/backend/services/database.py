from sqlalchemy.ext.asyncio import create_async_engine
from models.basicbase import Base
import asyncio
import utils.config
from models.email import Email
from models.question import Question
from models.results import Results
from models.task import Task
from models.user import *
from models.answer import *

database_filename = utils.config.get_config('database.filename')


db_params = 'sqlite+aiosqlite:///' + database_filename

engine = create_async_engine(db_params)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

def init_models_sync():
    print('###############################################')
    print('Database:', database_filename)
    print('###############################################')

    asyncio.run(init_models())

if __name__ == '__main__':
    init_models_sync()