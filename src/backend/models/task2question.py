from sqlalchemy import Column, Integer,ForeignKey,UniqueConstraint
from .basicbase import Base
class Task2Question(Base):
    __tablename__ = 'task2question'
    id = Column(Integer,primary_key=True)
    task = Column(Integer,ForeignKey('task.id'))
    question = Column(Integer,ForeignKey('question.id',ondelete='CASCADE'))
    UniqueConstraint('task','question',name='task2question_relation')

