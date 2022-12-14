from sqlalchemy import Column, Integer, String ,ForeignKey,DateTime,BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base
import datetime
MAX_TYPE_LENGTH = 24
MAX_CHOICES_LENGTH = 128
MAX_TEXT_LENGTH = 1024
MAX_NAME_LENGTH = 256
class Answer(Base):
    __tablename__ = 'answer'
    id = Column(BigInteger,primary_key=True,autoincrement=True)
    date_answered = Column(DateTime,default = datetime.datetime.now)
    question_id = Column(Integer,ForeignKey('question.id'))
    task_id = Column(Integer,ForeignKey('task.id'))
    respondent_id = Column(Integer,ForeignKey('user.id')) 
    question_type = Column(String(MAX_TYPE_LENGTH))
    answer_type = Column(String(MAX_TYPE_LENGTH))
    respondent_name = Column(String,MAX_NAME_LENGTH)
    __mapper_args__ = {
        'polymorphic_on':answer_type,
        'polymorphic_identity':'answer'
    }
    
class SingleChoiceAnswer(Answer):
    __tablename__ = 'singlechoiceanswer'
    id =Column(BigInteger,ForeignKey('answer.id'),primary_key = True)
    choice = Column(Integer)
    __mapper_args__ = {
        'polymorphic_identity':'singlechoiceanswer'
    }

class MultiChoiceAnswer(Answer):
    __tablename__ = 'multichoiceanswer'
    id =Column(BigInteger,ForeignKey('answer.id'),primary_key = True)
    choices = Column(String(MAX_CHOICES_LENGTH))
    __mapper_args__ = {
        'polymorphic_identity':'multichoiceanswer'
    }

class RankingAnswer(Answer):
    __tablename__ = 'rankinganswer'
    id =Column(BigInteger,ForeignKey('answer.id'),primary_key = True)
    ranking = Column(String(MAX_CHOICES_LENGTH))
    __mapper_args__ = {
        'polymorphic_identity':'rankinganswer'
    }

class OpenAnswer(Answer):
    __tablename__ = 'openanswer'
    id =Column(BigInteger,ForeignKey('answer.id'),primary_key = True)
    text = Column(String(MAX_TEXT_LENGTH))    
    __mapper_args__ = {
        'polymorphic_identity':'openanswer'
    }

class BoundingBoxAnswer(Answer):
    __tablename__ = 'boundingboxanswer'
    id =Column(BigInteger,ForeignKey('answer.id'),primary_key = True)
    top_left_x =  Column(Integer)
    top_left_y = Column(Integer)
    bottom_right_x = Column(Integer)
    bottom_right_y = Column(Integer)
