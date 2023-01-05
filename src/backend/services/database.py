from sqlalchemy.ext.asyncio import create_async_engine
from models.basicbase import Base
import asyncio
import utils.config
from models.email import *
from models.question import *
from models.task import *
from models.user import *
from models.answer import *

database_filename = utils.config.get_config('file_locations.database')


db_params = 'sqlite+aiosqlite:///' + database_filename

engine = create_async_engine(db_params)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

def init_models_sync(verbose=False):
    if verbose:
        print('#' * 80)
        print('Database at:', database_filename)
        print('#' * 80)


    asyncio.run(init_models())

if __name__ == '__main__':
    init_models_sync()