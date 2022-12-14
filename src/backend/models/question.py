from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base
MAX_NAME_LENGTH = 64
MAX_TYPE_LENGTH = 24
MAX_PROMPT_LENGTH = 256
MAX_RES_LENGTH = 512
MAX_OPT_LENGTH = 256
class Question(Base):
    """
    Questions are the units that make up a task.
    A question must have a prompt that is presented to the user.
    The user can then respond to the prompt using various methods.
    These methods are defined by the subclasses of `Question`.
    Questions may have a known answer, and the answer may be used
    to 
    """ 
    __tablename__ = 'question'
    id = Column(Integer,unique = True, primary_key=True,autoincrement=True)
    question_type = Column (String(MAX_TYPE_LENGTH))
    prompt = Column(String(MAX_PROMPT_LENGTH))
    resource = Column(String(MAX_RES_LENGTH))
    options = Column(String(MAX_OPT_LENGTH))
    id_in_task = Column(Integer)
    task_id = Column(Integer,ForeignKey('task.task_id'))
    answer = relationship('Answer',cascade = 'delete, delete-orphan')
    
    __mapper_args__ = {
        'polymorphic_on':question_type
    }
    
    def __init__(self, id_in_task,type, prompt, resource, options,task_id):
        self.id_in_task = id_in_task
        self.type = type
        self.prompt = prompt
        self.resource = str(resource)
        self.options = options
        self.task_id = task_id
    def dict(self):
        return {key: self.__dict__[key] for key in self.__dict__ if key[0] != '_'}
class MultipleChoice(Question):
    __tablename__ = 'multiplechoice'
    id = Column(Integer,ForeignKey('question.id'),primary_key = True)
    __mapper_args__ = {
        'polymorphic_identity': 'multi_choice'
    }

class SingeChoiceQuestion(Question):
    __tablename__ = 'singlechoicequestion'
    id = Column(Integer,ForeignKey('question.id'),primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'single_choice'
    }

class BoundingBoxQuestion(Question):
    __tablename__ = 'boundingboxquestion'
    id = Column(Integer,ForeignKey('question.id'),primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'bounding_box'
    }
class OpenQuestion(Question):
    __tablename__ = 'openquestion'
    id = Column(Integer,ForeignKey('question.id'),primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'open'
    }

