from sqlalchemy import Column, Integer, String ,DateTime,FLOAT,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base
from sqlalchemy.orm import relationship
from .user2task import *
import datetime

MAX_USERNAME_LENGTH = 64
HASH_LENGTH = 97 # len(hash('test'))
MAX_EMAIL_LENGTH = 320 # RFC
VERIFICATION_CODE_LENGTH = 6
MAX_USERTYPE_LENGTH = 20
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key = True,autoincrement=True)
    username = Column(String(MAX_USERNAME_LENGTH), unique=True)
    password_hashed = Column(String(HASH_LENGTH))
    email = Column(String(MAX_EMAIL_LENGTH))
    user_type = Column(String(MAX_USERTYPE_LENGTH))
    date_created = Column(DateTime,default = datetime.datetime.now)
    tokens = Column(FLOAT)
    __mapper_args__ = {
        'polymorphic_on':user_type,
        'polymorphic_identity':'user'
    }
    def __init__(self, username, password_hashed, email, user_type, status):
        self.username = username
        self.password_hashed = password_hashed
        self.email = email
        self.user_type = user_type
        self.status = status

class Requester(User):
    __tablename__ = 'requester'
    id = Column(Integer,ForeignKey('user.id'),primary_key = True)
    task_requested = relationship('Requester2Task',secondary=Requester2Task,cascade="delete, delete-orphan")
    __mapper_args__ = {
        'polymorphic_identity':'requester'
    }
class Respondent(User):
    __tablename__ = 'respondent'
    id = Column(Integer,ForeignKey('user.id'),primary_key = True)
    task_claimed = relationship('Respondent2Claim',secondary=Respondent2Claim,cascade="delete, delete-orphan")
    task_complete = relationship('Respondent2Complete',secondary=Respondent2Complete,cascade="delete, delete-orphan")
    __mapper_args__ = {
        'polymorphic_identity':'respondent'
    }
class Admin(User):
    __tablename__ = 'Admin'
    id = Column(Integer,ForeignKey('user.id'),primary_key = True)
    __mapper_args__ = {
        'polymorphic_identity':'admin'
    }