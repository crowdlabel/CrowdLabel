from sqlalchemy import Column, Integer, String ,DateTime
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base
MAX_NAME_LENGTH = 64

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer,unique = True, primary_key=True,autoincrement=True)
    name = Column(String(MAX_NAME_LENGTH))
    def __init__(self,name) -> None:
        self.name=name

