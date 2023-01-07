from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator
from email_validator import validate_email

import re


from models.user import MAX_USERNAME_LENGTH



class Username(BaseModel):
    username: str
    __chars = r'A-Za-z0-9_\.\_'
    __min_length = 3
    __pattern = re.compile(fr'[{__chars}]{{{__min_length},{MAX_USERNAME_LENGTH}}}')
    @validator('username')
    def username_format(cls, username):
        if not re.fullmatch(Username.__pattern, username):
            raise ValueError('Username format incorrect')
        return username
    class Config:
        schema_extra = {
            'example': {
                'username': 'johndoe',
            }
        }

class Email(BaseModel):
    email: str
    @validator('email')
    def email_format(cls, email):
        try:
            if validate_email(email=email, check_deliverability=False):
                return email
        except:
            pass

        raise ValueError('Email format incorrect')
    class Config:
        schema_extra = {
            'example': {
                'email': 'johndoe@example.com',
            }
        }

class Password(BaseModel):
    password: str
    __min_length = 8
    __max_length = 64
    __chars = r'\x20-\x7e' # printable chars excluding delete
    __pattern = re.compile(fr'[{__chars}]{{{__min_length},{__max_length}}}')
    @validator('password')
    def password_format(cls, password):
        if not re.fullmatch(Password.__pattern, password):
            raise ValueError('Password format incorrect')
        return password


class UserType(BaseModel):
    user_type: str
    @validator('user_type')
    def user_type_format(cls, user_type):
        if user_type not in set(['requester', 'respondent', 'admin']):
            raise ValueError('Invalid user_type, must be "requester", "respondent", or "admin"')
        return user_type
    class Config:
        schema_extra = {
            'example': {
                'user_type': 'respondent',
            }
        }

class VerificationCode(BaseModel):
    verification_code: str
    __pattern = r'\d{6}'
    @validator('verification_code')
    def verification_code_format(cls, verification_code):
        if not re.fullmatch(VerificationCode.__pattern, verification_code):
            raise ValueError('Verification code format invalid')
        return verification_code
    class Config:
        schema_extra = {
            'example': {
                'verification_code': '123456',
            }
        }   


class AvailabilityRequest(Username, Email):
    username: Optional[str]
    email: Optional[str]
    class Config:
        schema_extra = {
            'example': {
                'username': 'johndoe',
                'email': 'taken@example.com',
            }
        }

class AvailabilityResponse(BaseModel): 
    username: Optional[bool]
    email: Optional[bool]
    class Config:
        schema_extra = {
            'example': {
                'username': True,
                'email': False,
            }
        }

class RegistrationRequest(Username, Email, Password, UserType, VerificationCode):
    class Config:
        schema_extra = {
            'example': {
                'username': 'johndoe',
                'email': 'johndoe@example.com',
                'password': 'secret123',
                'user_type': 'respondent',
                'verification_code': '123456',
            }
        }


class RegistrationError(BaseModel):
    username: Optional[str]
    email: Optional[str]
    verification_code: Optional[str]
    class Config:
        schema_extra = {
            'example': {
                'username': 'exists',
                'email': 'exists',
                'verification_code': 'wrong',
            }
        }

class EditEmailRequest(VerificationCode,Password):
    new_email: str
    @validator('new_email')
    def email_format(cls, email):
        try:
            if validate_email(email=email, check_deliverability=False):
                return email
        except:
            pass

        raise ValueError('Email format incorrect')

    class Config:
        schema_extra = {
            'example': {
                'new_email': 'newemail@example.com',
                'verification_code': '123456',
                'password': 'secret123',
            }
        }

class EditPasswordRequest(BaseModel):
    old_password: str
    @validator('old_password')
    def old_password_format(cls, password):
        if not re.fullmatch(Password.__pattern, password):
            raise ValueError('Password format incorrect')
        return password
    new_password: str
    @validator('new_password')
    def new_password_format(cls, password):
        if not re.fullmatch(Password.__pattern, password):
            raise ValueError('Password format incorrect')
        return password
    class Config:
        schema_extra = {
            'example': {
                'old_password': 'secret123',
                'new_password': 'newsecret123',
            }
        }


class User(Username, Email, UserType):
    credits: float=0
    date_created: datetime
    password_hashed: str=''

    """ def __init__(self, user):
        super(User, self).__init__(
            username=user.username,
            email=user.email,
            credits=user.credits,
            date_created=user.date_created,
            password_hashed=user.password_hashed,
        ) """
        

    class Config:
        schema_extra = {
            'example': {
                'username': 'johndoe',
                'email': 'johndoe@example.com',
                'user_type': 'respondent',
                'credits': 0,
                'date_created': datetime(1970, 1, 1, 0, 0 , 0),
                'tested': False,
                'tasks_claimed': {1, 4},
                'tasks_completed': {2, 3},
            }
        }

class Requester(User):
    tasks_requested: set[int]=set() # list Task IDs
    user_type='requester'

    """ def __init__(self,user):
        super(Requester,self).__init__(user)
        self.user_type='requester' """

class Respondent(User):
    tested: bool=False
    user_type = 'respondent'

    tasks_claimed: set[int]=set() # list Task IDs
    tasks_completed: set[int]=set() # list Task IDs
    """ def __init__(self, user):
        super(Respondent, self).__init__(user)
        self.user_type = 'respondent' """

class Admin(Requester, Respondent):
    user_type = 'admin'
    """ def __init__(self, user):
        super(Admin, self).__init__(user) """

UserType = Requester | Respondent | Admin

USER_TYPES = {
    'requester': Requester,
    'respondent': Respondent,
    'admin': Admin,
}

class TransactionRequest(BaseModel):
    amount: float

    class Config:
        schema_extra = {
            'example': {
                'amount': 2.56
            }
        }