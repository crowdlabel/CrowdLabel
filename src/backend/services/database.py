from sqlalchemy import create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
Base = declarative_base()
#from utils.config import get_config

db_params = f"sqlite:///crowdlabel.db"

engine = create_engine(db_params)
def init_db():
    User.__table__.create(engine, checkfirst=True)


def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_db()
    init_db()
