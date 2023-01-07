from sqlalchemy.ext.asyncio import create_async_engine
from models.basicbase import Base
import asyncio
import utils.config
import pathlib
from models.email import *
from models.question import *
from models.task import *
from models.user import *
from models.answer import *

database_filename = utils.config.config['database_filename']

db_params = 'sqlite+aiosqlite:///' + database_filename
engine = create_async_engine(db_params)

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

def reset_db():
    asyncio.run(init_models())

def init_db():
    if not pathlib.Path(database_filename).is_file():
        reset_db()

init_db()

if __name__ == '__main__':
    reset_db()