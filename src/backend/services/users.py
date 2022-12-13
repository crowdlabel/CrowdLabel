import checkers.users
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
import models.user
from utils import hasher
from utils.emailsender import EmailSender
from sqlalchemy import select, update
from .fakedata import fake_users, fake_emails
import random
from .database import *
import schemas.users
from datetime import datetime

email_sender = EmailSender()

Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)

NO_DB = True


async def send_verification_email(email) -> bool:
    """
    Sends verification email
    
    Returns `True` if the email was sent successfully,
    `False` otherwise
    """

    if not checkers.users.check_email_format(email):
        return False

    verification_code = str(random.randint(0, 999999)).rjust(6, '0')

    # TODO: add email and verification code to db,
    # or update the verification code of an existing email

    if NO_DB:
        fake_emails[email] = verification_code
    else:
        async with con.begin():
            res= await con.execute(select(Email).where(Email.email==email))
            target = res.scalars().first()
            if target is None:
                email_create = Email(email=email,code = verification_code)
                con.add(email_create)
                await con.commit()
            else:
                print(f'update code from {target.verification_code} to {verification_code}')
                target.verification_code = verification_code
                await con.flush()
                con.expunge(target)
                
    email_sender.send_email(
        'CrowdLabel 邮箱验证码',
        verification_code,
        'noreply@crowdlabel.org',
        [email]
    )

    return True


async def check_verification_code(email: str, verification_code: str):
    if NO_DB:
        return email in fake_emails and fake_emails[email] == verification_code
    else:
        async with con.begin():
            res= await con.execute(select(Email).where(Email.email==email))
            target = res.scalars().first()
            if target is None:
                return {
                    'arg': 'email',
                    'error': 'notfound'
                }
            if target.verification_code != verification_code:
                return {
                    'arg': 'verification_code',
                    'error': 'mismatch'
                }
            con.add(user)
            await con.commit()

async def create_user(
    username: str,
    email: str,
    password: str,
    user_type: str,
    verification_code: str,
) -> tuple[list[str]] | None:
    # get the arguments as a dictionary
    args = locals()


    errors = {}

    # check arguments' formats
    for arg in args:
        if not checkers.users.format_checkers[arg](args[arg]):
            errors[arg] = 'format'

    # check existance
    if 'username' not in errors and await username_exists(username):
        errors['username'] = 'exists'
    if 'email' not in errors and await email_exists(email):
        errors['email'] = 'exists'
    
    if errors:
        return errors

    if not check_verification_code(email, verification_code):
        errors['verification_code'] = 'wrong'
        return errors

    if user_type in ['0', 'respondent']:
        new_user = schemas.users.Respondent()
    elif user_type in ['1', 'requester']:
        new_user = schemas.users.Requester()
    new_user.username = username
    new_user.email = email
    new_user.password_hashed = hasher.hash(password)
    new_user.date_created = datetime.utcnow()
    fake_users.append(new_user)

    


async def authenticate(username: str, password: str) -> bool:


    for user in fake_users:
        if (user.username == username and 
            hasher.verify(user.password_hashed, password)):
            return True

    return False

    con = scoped_session(Connection)
    res = con.query(User).filter(User.username == username).all()

    if (len(res) == 0):
        return False

    user = res[0]

    return verify(user.password, password)

async def get_user(username: str) -> dict | None:
    """
    Gets the information about a user
    
    Also needs to consider if the user is logged in,
    and if the user is requesting their own info

    Returns:
    """

    for user in fake_users:
        if user.username == username:
            return user
    return None

    info = {
        'username': '',
        'email': '',
        'type': '',
        'status': '',
        'tasks_completed': []
    }

    res = con.query(User).filter(User.username == username).all()
    if len(res) == 0:
        return {}
    pass

async def set_user_info(new_info: dict) -> bool:
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

async def username_exists(username: str) -> bool:

    for user in fake_users:
        if user.username == username:
            return True
    return False

    if not check_username_format(username):
        return False
    async with con.begin():
        res= await con.execute(select(User).where(User.username==username))
        target = res.scalars().first()
    if target is None:
        return False
    return True

async def email_exists(email: str) -> bool:

    for user in fake_users:
        if user.email == email:
            return True
    return False

    if not check_email_format(email):
        return False
    async with con.begin():
        res= await con.execute(select(User).where(User.email==email))
        target = res.scalars().first()
    if target is None:
        return False
    return True

