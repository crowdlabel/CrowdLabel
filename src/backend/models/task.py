from sqlalchemy import Column, Integer, String ,DateTime,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .basicbase import Base
from .user2task import *
import schemas.tasks
import datetime
MAX_NAME_LENGTH = 64
MAX_DETAIL_LENGTH = 512
MAX_PATH_LENGTH =128
MAX_TAGS_LENGTH = 256
class Task(Base):
    __tablename__ = 'task'
    task_id = Column(Integer,unique = True, primary_key=True,autoincrement=True)
    requester = Column(String(MAX_NAME_LENGTH))
    introduction =Column(String(MAX_NAME_LENGTH))
    description  = Column(String(MAX_DETAIL_LENGTH))
    name = Column(String(MAX_NAME_LENGTH))
    cover_image = Column(String(MAX_PATH_LENGTH))
    date_created = Column(DateTime,default = datetime.datetime.now)
    credits = Column(Float)
    tags = Column(String(MAX_TAGS_LENGTH))
    responses_required = Column(Integer)
    resource_path = Column(String(MAX_PATH_LENGTH))
    requester_id = Column(Integer ,ForeignKey('requester.id'))

    #results = relationship('Results',cascade = 'all,delete-orphan')
    questions = relationship('Question')    
    respondents_claimed = relationship('Respondent',secondary='respondent2claim',cascade="delete, delete-orphan",single_parent = True, overlaps="task_complete, task_claimed")
    respondents_complete = relationship('Respondent',secondary = 'respondent2complete',cascade="delete, delete-orphan",single_parent = True, overlaps="task_complete")
   
    def __init__(self,task_schema:schemas.tasks.Task,resource_path):
        self.task_id = task_schema.task_id
        self.requester = task_schema.requester
        self.introduction = task_schema.introduction
        self.description = task_schema.description
        self.name = task_schema.name
        self.cover_image = task_schema.cover_image
        self.date_created = task_schema.date_created
        self.credits = task_schema.credits
        self.tags = '|'.join(task_schema.tags)
        self.responses_required = task_schema.responses_required
        self.resource_path = resource_path