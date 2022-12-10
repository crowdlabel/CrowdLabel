from datetime import datetime
from pydantic import BaseModel
from .tasks import Task


class Email(BaseModel):
    email: str

class AvailabilityRequest(BaseModel):
    username: str | None
    email: str | None
class AvailabilityResponse(BaseModel): 
    username: bool
    email: bool


class RegistrationResponse(BaseModel):
    username: str
    email: str
    user_type: int
class RegistrationRequest(RegistrationResponse):
    password: str
    verification_code: int



class UserInfoRequest:
    username: str




class User(BaseModel):
    username: str
    email: str
    password_hashed: str
    creation_date: datetime
    user_type: str
class Admin(User):
    user_type='admin'

class TokenUser(User):
    tokens: int

class Requester(TokenUser):
    user_type='requester'
    tasks_requested: list[Task]
class Respondent(TokenUser):
    user_type='respondent'
    tested: bool
    tasks_claimed: list[Task]
    tasks_completed: list[Task]