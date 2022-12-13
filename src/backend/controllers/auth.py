from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from utils.config import get_config
from .jsonerror import JSONError, forbidden
import services.users as us
from schemas.auth import Token
from schemas.users import User




router = APIRouter()



# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/





SECRET_KEY = get_config('auth.key')
ALGORITHM = get_config('auth.algorithm')
ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(minutes=get_config('auth.access_token_expire_minutes'))



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE_MINUTES
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(user_types: list=[]) -> User:
    """
    Returns a function to be used by API endpoints
    """
    async def get_current_user_types(token: str = Depends(oauth2_scheme)):
        """
        Performs two tasks:
        1. verifies the token, proving the request is from a logged-in user
        2. raises exception if the logged-in user's type isn't in `user_types`
        Returns the user
        """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        forbidden_exception = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Forbidden',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get('sub')
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        user = await us.get_user(username)

        if not user:
            raise credentials_exception

        if user_types:
            if not (user.user_type == 'admin' or user.user_type in user_types):
                raise forbidden_exception
        return user
        
    return get_current_user_types



invalid_credentials = JSONError(
    status.HTTP_401_UNAUTHORIZED,
    {'description': 'Username or password incorrect.'}
)
@router.post('/login',
    responses={
        invalid_credentials.status_code: invalid_credentials.response_doc(),
    },
    response_model=Token,
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print('logging in')
    if not await us.authenticate(form_data.username, form_data.password):
        return invalid_credentials.response()
    access_token = create_access_token(
        data={'sub': form_data.username},
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/token',
    responses={
        invalid_credentials.status_code: invalid_credentials.response_doc(),
    },
    response_model=Token,
)
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    """ same function as the `login` endpoint """
    return await login(form_data)