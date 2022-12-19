from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Email(BaseModel):
    email: str
    class Config:
        schema_extra = {
            'example': {
                'email': 'johndoe@example.com',
            }
        }

class AvailabilityRequest(BaseModel):
    username: Optional[str | None]
    email: Optional[str | None]
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

class RegistrationRequest(BaseModel):
    username: str
    email: str
    password: str
    user_type: str
    verification_code: str

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
    password: Optional[str]
    user_type: Optional[str]
    verification_code: Optional[str]
    class Config:
        schema_extra = {
            'example': {
                'username': 'exists',
                'email': 'exists',
                'user_type': 'format',
                'password': 'format',
                'verification_code': 'wrong',
            }
        }


class User(BaseModel):
    username: str=''
    email: str=''
    user_type: str=''
    credits: float=0
    date_created: datetime=datetime.utcnow()

    def __init__(self, user):
        super(User, self).__init__(
            username=user.username,
            email=user.email,
            credits=user.credits,
            date_created=user.date_created,
            password_hashed=user.password_hashed
        )


    async def edit_user_info(new_info: dict) -> bool:
        """
        Edits self using the new user
        """

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
    user_type = 'requester'
    tasks_requested: set[int]=set() # list Task IDs
    def __init__(self,user):
        super(Requester,self).__init__(user)

class Respondent(User):
    user_type = 'respondent'
    tested: bool = False
    tasks_claimed: set[int] = set()  # set of Task IDs
    tasks_completed: set[int] = set()  # set of Task IDs

    def __init__(self, user):
        super(Respondent, self).__init__(user)


class Admin(Requester, Respondent):
    user_type = 'admin'
    def __init__(self, user):
        super(Admin, self).__init__(user)


USER_TYPES = {
    'requester': Requester,
    'respondent': Respondent,
    'admin': Admin,
}