from fastapi.responses import JSONResponse
from fastapi import status

class JSONError:
    def __init__(self, status_code, description):
        self.status_code = status_code
        self.description = description
    def response(self):
        return JSONResponse(
            content = {'description': self.description},
            status_code = self.status_code,
        )
    def responses(self):
        return {self.status_code: self.response_doc()}
    def response_doc(self):
        return {
            'description': self.description,
            'content': {
                'application/json': {
                    'example': {'description': self.description}
                }
            }
        }

def response_doc(description):
    return {
        'description': description,
        'content': {
            'application/json': {
                'example': {'description': description}
            }
        }
    }

def json_response(status_code, description):
    return JSONResponse(
        content={'description': description},
        status_code=status_code,
    )



unauthorized = JSONError(
    status.HTTP_401_UNAUTHORIZED,
    {'description': 'Unauthenticated. Try checking your token, or login again.'}
)

forbidden = JSONError(
    status.HTTP_403_FORBIDDEN,
    {'description': 'You have insufficient permissions to access this content.'}
)

rate_limit_error = JSONError(
    status.HTTP_429_TOO_MANY_REQUESTS,
    {'description': 'Too many requests.'}
)