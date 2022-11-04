from checkers.user import *
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from utils.hasher import *
from utils.emailverification import *

from .database import *
Connection = sessionmaker(bind=engine)


def create_user(username, email, password, usertype):
    # get the arguments as a dictionary
    args = locals()

    # check arguments' formats
    for arg in args:
        if not format_checkers[arg](args[arg]):
            return {
                'arg': arg,
                'error': 'format',
            }

    # check existance
    if username_exists(username):
        return {
            'arg': 'username',
            'error': 'exists',
        }
    if email_exists(email):
        return {
            'arg': 'email',
            'error': 'exists'
        }

    password = hash(password)
    con = scoped_session(Connection)
    
    verification_code = generate_verification_code()

    user = User(
        username=username,
        password=password,
        email=email,
        usertype=usertype,
        status=0,
        verification_code=verification_code
    )
    con.add(user)
    con.commit()
    con.close()

    send_verification_email(email, verification_code)

    return {
        'arg': 'ok',
        'error': 'ok',
    }

async def check_credentials(username: str, password: str) -> bool:
    return username == 'username' and password == 'password'
    con = scoped_session(Connection)
    res = con.query(User).filter(User.username == username).all()

    if (len(res) == 0):
        return False

    user = res[0]

    return verify(user.password, password)

async def login(username: str, password: str) -> bool | str:
    """
    Logins in a user
    Returns a jwt if login successful
    Returns `False` otherwise
    """
    if (not check_username_format(username) or
        not check_password_format(password)):
        return False

    if not await check_credentials(username, password):
        return False

    jwt = get_jwt(username)

    return jwt

def get_user_info(username: str) -> dict:
    """
    Gets the information about a user
    
    Also needs to consider if the user is logged in,
    and if the user is requesting their own info

    Returns:
    """
    info = {
        'username': '',
        'email': '',
        'type': '',
        'status': '',
        'tasks_completed': []
    }

    con = scoped_session(Connection)
    res = con.query(User).filter(User.username == username).all()
    if len(res) == 0:
        return {}
    pass

def get_jwt(username: str) -> str:
    return 'jwt_test'

def set_user_info(new_info: dict) -> bool:
    """
    Sets user info

    `new_info`: is a dict where the field to be set, and the value is the new info
    Returns True if the info was set correctly

    E.g.:
    {
        'email': 'example@gmail.com',
        'password': 'new_password'
    }
    Will update the email and password

    If the field doesn't exist, or the value fails checks, return False

    """


def verify_email(email: str, verification_code: str) -> bool:
    con = scoped_session(Connection)
    res = con.query(User).filter(User.email == email).all()
    if len(res) == 1:
        user = res[0]
    else:
        return False

    if user.verification_code != verification_code:
        return False

    
    # TODO: update user verification status


    return True




def __field_exists(field, value):
    con = scoped_session(Connection)
    res = con.query(User).filter(User.__dict__[field] == value).all()
    if len(res) > 1:
        raise ValueError(f'Duplicate {field}: {str(res.all()[0])}')
    else:
        return len(res) == 1

def username_exists(username):
    return __field_exists('username', username)

def email_exists(email):
    return __field_exists('email', email)