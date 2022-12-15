from sqlalchemy import Column, Integer, String ,DateTime,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .basicbase import Base
from .user2task import *
from .task2question import *
import datetime
MAX_NAME_LENGTH = 64
MAX_DETAIL_LENGTH = 512
MAX_PATH_LENGTH =128
MAX_TAGS_LENGTH = 256
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer,unique = True, primary_key=True,autoincrement=True)
    creator = Column(String(MAX_NAME_LENGTH))
    introduction =Column(String(MAX_NAME_LENGTH))
    description  = Column(String(MAX_DETAIL_LENGTH))
    name = Column(String(MAX_NAME_LENGTH))
    cover_path = Column(String(MAX_PATH_LENGTH))
    date_created = Column(DateTime,default = datetime.datetime.now)
    credits = Column(Float)
    tags = Column(String(MAX_TAGS_LENGTH))
    response_required = Column(Integer)
    file_path = Column(String(MAX_PATH_LENGTH))


    results = relationship('Results',cascade = 'all,delete-orphan')
    questions = relationship('Question',secondary='task2question',cascade="delete, delete-orphan",single_parent = True)    
    requester = relationship('Requester',secondary='requester2task',cascade="delete, delete-orphan",single_parent = True)
    respondent_claimed = relationship('Respondent',secondary='respondent2claim',cascade="delete, delete-orphan",single_parent = True)
    respondent_complete = relationship('Respondent',secondary = 'respondent2complete',cascade="delete, delete-orphan",single_parent = True)
   


