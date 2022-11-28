from sqlalchemy import Column, Integer, String ,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .basicbase import Base
MAX_NAME_LENGTH = 64
MAX_DETAIL_LENGTH = 512
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer,unique = True, primary_key=True,autoincrement=True)
    creator = Column(String(MAX_NAME_LENGTH))
    details  = Column(String(MAX_DETAIL_LENGTH))
    name = Column(String(MAX_NAME_LENGTH))
    questions = relationship('Question')
    results = relationship('Results')
    def __init__(self,name,creator,detail) -> None:
        self.name=name
        self.creator = creator
        self.details = detail

