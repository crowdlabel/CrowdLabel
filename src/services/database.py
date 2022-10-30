from sqlalchemy import create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from utils.config import get_config

db_params = f"mysql+pymysql://{get_config('db.user')}:{get_config('db.password')}\
    @{get_config('db.host')}:{get_config('db.port')}/crowdlabel?charset=utf8"

engine = create_engine(db_params)
def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_db()
    init_db()
