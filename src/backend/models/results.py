from sqlalchemy import Column, Integer, String ,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base
from sqlalchemy.orm import relationship

import datetime


MAX_USERNAME_LENGTH = 64
HASH_LENGTH = 97 # len(hash('test'))
MAX_EMAIL_LENGTH = 320 # RFC
VERIFICATION_CODE_LENGTH = 6

class Results(Base):
    __tablename__ = 'result'
    id = Column(Integer,unique=True,primary_key = True)
    name = Column(String(MAX_USERNAME_LENGTH))
    task_id = Column(Integer,ForeignKey('task.id'))
    date_created = Column(DateTime,default = datetime.datetime.now)
    date_download = Column(DateTime)
    child_result = relationship('ChildResults')
    def __init__(self, task_id, name):
        self.task_id = task_id 
        self.name = name 
