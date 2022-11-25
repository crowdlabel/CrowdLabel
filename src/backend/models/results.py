from sqlalchemy import Column, Integer, String ,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base
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
    date_created = Column(DateTime)
    date_download = Column(DateTime,default = datetime.now)
    def __init__(self, task_id, name):
        self.tasK_id = id 
        self.name = name 
