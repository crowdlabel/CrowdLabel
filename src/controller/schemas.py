from pydantic import BaseModel
from fastapi import Response, status

class JSONError:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content
    def description(self):
        return self.content['description']
    def response(self):
        return Response(
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


class JWT(BaseModel):
    jwt: str

login_error = JSONError(
    status.HTTP_401_UNAUTHORIZED,
    {'description': 'Username or password incorrect.'}
)


