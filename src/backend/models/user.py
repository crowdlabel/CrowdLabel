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
MAX_TOKEN_LENGTH = 512
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key = True,autoincrement=True)
    username = Column(String(MAX_USERNAME_LENGTH), unique=True)
    password_hashed = Column(String(HASH_LENGTH))
    email = Column(String(MAX_EMAIL_LENGTH))
    user_type = Column(String(MAX_USERTYPE_LENGTH))
    date_created = Column(DateTime,default = datetime.datetime.now)
    credits = Column(FLOAT)
    token = Column(String(MAX_TOKEN_LENGTH))
    __mapper_args__ = {
        'polymorphic_on':user_type,
        'polymorphic_identity':'user'
    }

    # def __init__(self, username, password_hashed, email, user_type, status):
    #     self.username = username
    #     self.password_hashed = password_hashed
    #     self.email = email
    #     self.user_type = user_type
    #     self.status = status

class Requester(User):
    __tablename__ = 'requester'
    id = Column(Integer,ForeignKey('user.id'),primary_key = True)
    task_requested = relationship('Task')
    __mapper_args__ = {
        'polymorphic_identity':'requester'
    }

class Respondent(User):
    __tablename__ = 'respondent'
    id = Column(Integer,ForeignKey('user.id'),primary_key = True)
    tested = Column(Integer)
    task_claimed = relationship('Task',secondary='respondent2claim',cascade="delete, delete-orphan",single_parent = True, overlaps="task_complete")
    task_complete = relationship('Task',secondary='respondent2complete',cascade="delete, delete-orphan",single_parent = True)
    __mapper_args__ = {
        'polymorphic_identity':'respondent'
    }
class Admin(User):
    __tablename__ = 'Admin'
    id = Column(Integer,ForeignKey('user.id'),primary_key = True)
    __mapper_args__ = {
        'polymorphic_identity':'admin'
    }