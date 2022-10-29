from checkers.user import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from database import User
from password import hash, verify
from emailverification import generate_verification_code, send_verification_email
engine = create_engine(
    "mysql+pymysql://root:cxq1974328@127.0.0.1:3306/crowdlabel?charset=utf8"
)
Connection = sessionmaker(bind=engine)

"""
There are two types of users:
    - Requester: creates tasks to be completed
    - Worker: completes tasks

class User:
    def __init__(self,
            username,
            password,
            name,
            email,
            phone) -> None:
        pass

class Requester(User):
    def __init__(self) -> None:
        super().__init__()

class Contractor(User):
    def __init__(self) -> None:
        super().__init__()

"""


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


def create_user(username, email, password, usertype):
    args = locals()
    for arg in args:
        if not format_checkers[arg](args[arg]):
            return arg

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

    return 'ok'

def verify_email(username, email, verification_code):
    con = scoped_session(Connection)
    res = con.query(User).filter(User.username == username).all()
    if len(res) == 1:
        user = res[0]
    else:
        return 'bad'

    if user.email == email and user.verification_code == verification_code:
        # TODO: update user status
        return 'ok'

    return 'bad'

def correct_credentials(username, password):
    con = scoped_session(Connection)
    res = con.query(User).filter(User.username == username).all()

    if (len(res) == 0):
        return False

    user = res[0]

    return verify(user.password, password)


def field_exists(field, value):
    con = scoped_session(Connection)
    res = con.query(User).filter(User.__dict__[field] == value).all()
    if len(res) > 1:
        raise ValueError(f'Duplicate {field}: {str(res.all()[0])}')
    else:
        return len(res) == 1

def username_exists(username):
    return field_exists('username', username)

def email_exists(email):
    return field_exists('email', email)