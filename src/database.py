from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    username = Column(String(64), unique=True, primary_key=True)
    password = Column(String(1024))
    email = Column(String(64))
    type = Column(Integer)
    status = Column(Integer)

    def __init__(self, username, password, email, type, status):
        self.username = username
        self.password = password
        self.email = email
        self.type = type
        self.status = status


def init_db():
    engine = create_engine(
        "mysql+pymysql://root:cxq1974328@127.0.0.1:3306/crowdlabel?charset=utf8")
    Base.metadata.create_all(engine)


def drop_db():

    engine = create_engine(
        "mysql+pymysql://root:cxq1974328@127.0.0.1:3306/crowdlabel?charset=utf8"
    )

    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_db()
    init_db()
