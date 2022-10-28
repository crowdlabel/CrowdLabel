from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from checkers.user import MAX_USERNAME_LENGTH

class User(Base):
    __tablename__ = 'user'
    username = Column(String(MAX_USERNAME_LENGTH), unique=True, primary_key=True)
    password = Column(String(1024))
    email = Column(String(320))
    usertype = Column(Integer)
    status = Column(Integer)

    def __init__(self, username, password, email, usertype, status):
        self.username = username
        self.password = password
        self.email = email
        self.usertype = usertype
        self.status = status


def init_db():
    engine = create_engine(
        "mysql+pymysql://root:cxq1974328@127.0.0.1:3306/crowdlabel?charset=utf8"
    )
    Base.metadata.create_all(engine)


def drop_db():

    engine = create_engine(
        "mysql+pymysql://root:cxq1974328@127.0.0.1:3306/crowdlabel?charset=utf8"
    )
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_db()
    init_db()
