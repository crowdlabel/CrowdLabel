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

login_error = JSONError(
    status.HTTP_401_UNAUTHORIZED,
    {'description': 'Username or password incorrect.'}
)

authentication_error = JSONError(
    status.HTTP_401_UNAUTHORIZED,
    {'description': 'Unauthenticated. Try checking your token, or login again.'}
)

forbidden_error = JSONError(
    status.HTTP_403_FORBIDDEN,
    {'description': 'You have insufficient permissions to access the content.'}
)

rate_limit_error = JSONError(
    status.HTTP_429_TOO_MANY_REQUESTS,
    {'description': 'Too many requests.'}
)