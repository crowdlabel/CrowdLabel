from checkers.user import *
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from utils.hasher import *
from utils.emailsender import EmailSender

email_sender = EmailSender()

from .database import *
Connection = sessionmaker(bind=engine)

import random

def send_verification_email(email, verification_code) -> bool:

    if not check_email_format(email):
        return False

    verification_code = str(random.randint(0, 999999)).rjust(6, '0')

    # TODO: add email and verification code to db,
    # or update the verification code of an existing email

    email_sender.send_email(
        'CrowdLabel 邮箱验证码',
        verification_code,
        'noreply@crowdlabel.org',
        [email]
    )


    return True


def create_user(
    username: str,
    email: str,
    password: str,
    user_type: int,
    verification_code: str,
):

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


    # check verification code


    # TODO: check if `email` and `verification_code` match in the db

    password_hashed = hash(password)
    con = scoped_session(Connection)
    

    

    user = User(
        username,
        password_hashed,
        email,
        user_type,
        status=0,
    )
    
    con.add(user)
    con.commit()
    con.close()

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

def set_user_info(new_info: dict) -> bool:
    """
    Sets user info

    `new_info`: is a dict where the key is the field to be set,
                and the value is the new info

    Returns True if the info was set correctly

    E.g.:
    {
        'email': 'example@gmail.com',
        'password': 'new_password'
    }
    Will update the email and password

    If the field doesn't exist, or the value fails checks, return False

    """



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