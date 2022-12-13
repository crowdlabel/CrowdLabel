from datetime import datetime
from pydantic import BaseModel, validator
from .tasks import Task

import checkers.users

class Email(BaseModel):
    email: str

class AvailabilityRequest(BaseModel):
    username: str | None
    email: str | None
class AvailabilityResponse(BaseModel): 
    username: bool
    email: bool


class RegistrationRequest(BaseModel):
    username: str
    email: str
    user_type: str
    password: str
    verification_code: str
    @validator('username')
    def __username(cls, username):
        if not checkers.users.check_username_format(username):
            raise ValueError('Username format incorrect')
        return username
    @validator('email')
    def __email(cls, email):
        if not checkers.users.check_email_format(email):
            raise ValueError('Email format incorrect')
        return email
    @validator('user_type')
    def __user_type(cls, user_type):
        if not checkers.users.check_user_type_format(user_type):
            raise ValueError('User type format incorrect')
        return user_type
    @validator('password')
    def __password(cls, password):
        if not checkers.users.check_password_format(password):
            raise ValueError('Password format incorrect')
        return password
    @validator('verification_code')
    def __verification_code(cls, verification_code):
        if not checkers.users.check_verification_code_format(verification_code):
            raise ValueError('Verification code format incorrect')
        return verification_code


class RegistrationResponse(BaseModel):
    username: str=''
    email: str=''
    user_type: str=''
    date_created: datetime=datetime.utcnow()



class User(BaseModel):
    username: str=''
    email: str=''
    date_created: datetime=datetime.utcnow()
    user_type: str=''
    tokens: float=0
    password_hashed: str=''

class Requester(User):
    user_type='requester'
    tasks_requested: list[int]=[] # list Task IDs
class Respondent(User):
    user_type='respondent'
    tested: bool=False
    tasks_claimed: list[int]=[] # list Task IDs
    tasks_completed: list[int]=[] # list Task IDs

class Admin(Requester, Respondent):
    pass