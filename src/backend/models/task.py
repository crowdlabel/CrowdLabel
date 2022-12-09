from sqlalchemy import Column, Integer, String ,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .basicbase import Base
MAX_NAME_LENGTH = 64
MAX_DETAIL_LENGTH = 512
MAX_PATH_LENGTH =128
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer,unique = True, primary_key=True,autoincrement=True)
    type = Column(Integer)
    creator = Column(String(MAX_NAME_LENGTH))
    introduction =Column(String(MAX_NAME_LENGTH))
    details  = Column(String(MAX_DETAIL_LENGTH))
    name = Column(String(MAX_NAME_LENGTH))
    path = Column(String(MAX_PATH_LENGTH))
    questions = relationship('Question')
    results = relationship('Results')
    def __init__(self,name,creator,detail,introduction,type,path) -> None:
        self.name=name
        self.creator = creator
        self.introduction = introduction
        self.details = detail
        self.type = type
        self.path = path

