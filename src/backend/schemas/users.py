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
