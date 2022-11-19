from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base
MAX_RESULT_LENGTH = 512

class ChildResults(Base):
    __tablename__ = 'childResult'
    id = Column(Integer, unique=True, primary_key=True)
    response = Column(String(MAX_RESULT_LENGTH))
    result_id = Column(Integer,ForeignKey('result.id'))
    def __init__(self, id, response,result_id):
        self.id = id 
        self.response = response
        self.result_id = result_id