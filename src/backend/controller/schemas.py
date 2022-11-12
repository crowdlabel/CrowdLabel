from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import status

class JSONError:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content
    def description(self):
        return self.content['description']
    def response(self):
        return JSONResponse(
            content = self.content,
            status_code = self.status_code,
        )
    def response_doc(self):
        return {
            'description': self.description(),
            'content': {
                'application/json': {
                    'example': {'description': self.description()}
                }
            }
        }


class Email(BaseModel):
    email: str


class Credentials(BaseModel):
    username: str
    password: str

class Registration(Email, Credentials):
    usertype: int

class AuthenticatedRequest(BaseModel):
    jwt: str

class UserInfoRequest(AuthenticatedRequest):
    username: str

class JWT(BaseModel):
    jwt: str

class AuthenticatedRequest(BaseModel):
    jwt: str

class Task(AuthenticatedRequest):
    id: str

login_error = JSONError(
    status.HTTP_401_UNAUTHORIZED,
    {'description': 'Username or password incorrect.'}
)

authentication_error = JSONError(
    status.HTTP_401_UNAUTHORIZED,
    {'description': 'Unauthenticated. Try checking your JWT.'}
)

forbidden_error = JSONError(
    status.HTTP_403_FORBIDDEN,
    {'description': 'You have insufficient permissions to access the content.'}
)

class Availability(BaseModel):
    username: str | None
    email: str | None

rate_limit_error = JSONError(
    status.HTTP_429_TOO_MANY_REQUESTS,
    {'description': 'Too many requests.'}
)