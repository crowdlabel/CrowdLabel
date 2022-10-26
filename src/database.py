from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    username = Coloum(String(64), unique=True)
    password = Coloum(String(64))
    email = Coloum(String(64))
    type = Coloum(Integer)
    status = Coloum(Integer)

    def __init__(self, username, password, email, type, status):
        self.username = username
        self.password = password
        self.email = email
        self.type = type
        self.status = status
        self.engine = create_engine(
            "mysql://root:cxq1974328@127.0.0.1/crowdlabel?charset=utf-8")
        Base.metadata.create_all(self.engine)
