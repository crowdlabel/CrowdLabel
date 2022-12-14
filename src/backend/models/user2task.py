from sqlalchemy import Column, Integer,ForeignKey,UniqueConstraint
from .basicbase import Base
class Requester2Task(Base):
    __tablename__ = 'requester2task'
    id = Column(Integer,primary_key=True)
    requester = Column(Integer,ForeignKey('requester.id',ondelete='CASCADE'))
    task = Column(Integer,ForeignKey('task.id'))
    UniqueConstraint('requester','task',name='requester2task_relation')

class Respondent2Claim(Base):
    __tablename__ = 'respondent2claim'
    id = Column(Integer,primary_key=True)
    respondent = Column(Integer,ForeignKey('respondent.id',ondelete='CASCADE'))
    task = Column(Integer,ForeignKey('task.id'))
    UniqueConstraint('respondent','task',name='respondent2claim_relation')
    
class Respondent2Complete(Base):
    __tablename__ = 'respondent2complete'
    id = Column(Integer,primary_key=True)
    respondent = Column(Integer,ForeignKey('respondent.id',ondelete='CASCADE'))
    task = Column(Integer,ForeignKey('task.id'))
    UniqueConstraint('respondent','task',name='respondent2complete_relation')