import checkers.users
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
import utils.hasher
import utils.emailsender
from sqlalchemy import select, update
import random
from .database import *
import schemas.users
from datetime import datetime
from pydantic import BaseModel


Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)

NO_DB = True

fake_users = [
    schemas.users.Respondent(
        username='johndoe',
        email='johndoe@example.com',
        password_hashed=hash('secret'),
        date_created=datetime(2022, 10, 9, 10, 10),
        credits=0,
        tested=True,
        tasks_claimed=[],
        tasks_completed=[]
    ),
    schemas.users.Requester(
        username='requester1',
        email='requester1@example.com',
        password_hashed=hash('secret'),
        date_created=datetime(2022, 10, 9, 10, 10),
        credits=0,
        tasks_requested=[1],
    ),
    schemas.users.Admin(
        username='admin',
        email='admin@example.com',
        password_hashed=hash('secret'),
        date_created=datetime(2022, 10, 10, 10, 10, 10),
        credits=0,
        tasks_requested=[],
    )
]

fake_emails = {
    'me@georgetian.com': '000000'
}

class Users:

    def __init__(self):
        self.__email_sender = utils.emailsender.EmailSender()

    async def send_verification_email(self, email) -> bool:
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
            # TODO: check?
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
                    
        self.__email_sender.send_email(
            'CrowdLabel 邮箱验证码',
            verification_code,
            'noreply@crowdlabel.org',
            [email]
        )

        return True


    async def check_verification_code(self, email: str, verification_code: str):
        if NO_DB:
            return email in fake_emails and fake_emails[email] == verification_code
        else:
            # TODO: check?
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
                #con.add(user)
                await con.commit()

    async def create_user(self, 
        username: str,
        email: str,
        password: str,
        user_type: str,
        verification_code: str,
    ) -> User | dict:
        '''
        Creates a new user
        If successful, returns User object
        If unsuccessful, returns a dict with the fields along with their error message
        '''
        # get the arguments as a dictionary
        args = locals()


        errors = {}

        # check arguments' formats
        for arg in args:
            if not checkers.users.format_checkers[arg](args[arg]):
                errors[arg] = 'format'

        # check existance
        if 'username' not in errors and await self.username_exists(username):
            errors['username'] = 'exists'
        if 'email' not in errors and await self.email_exists(email):
            errors['email'] = 'exists'
        
        if errors:
            return errors

        if not await self.check_verification_code(email, verification_code):
            errors['verification_code'] = 'wrong'
            return errors





        if NO_DB:
            if user_type in ['0', 'respondent']:
                new_user = schemas.users.Respondent()
            elif user_type in ['1', 'requester']:
                new_user = schemas.users.Requester()
            new_user.username = username
            new_user.email = email
            new_user.password_hashed = utils.hasher.hash(password)
            new_user.date_created = datetime.utcnow()
            fake_users.append(new_user)
        else:
            pass
            # TODO: add new user to database
        


    async def authenticate(self, username: str, password: str) -> bool:


        if NO_DB:
            for user in fake_users:
                if (user.username == username and 
                    utils.hasher.verify(user.password_hashed, password)):
                    return True
            return False
        else:
            # TODO: check?
            con = scoped_session(Connection)
            res = con.query(User).filter(User.username == username).all()

            if (len(res) == 0):
                return False

            user = res[0]

            return utils.hasher.verify(user.password, password)

    async def get_user(self, username: str) -> User | None:
        """
        Returns User object, or None if user not found
        """

        if NO_DB:
            for user in fake_users:
                if user.username == username:
                    return user
            return None
        else:
            # TODO: check
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


    async def username_exists(self, username: str) -> bool:
        '''
        Returns `True` if the username already exists
        '''
        if NO_DB:

            for user in fake_users:
                if user.username == username:
                    return True
            return False
        else:
            # TODO: check
            if not checkers.users.check_username_format(username):
                return False
            async with con.begin():
                res= await con.execute(select(User).where(User.username==username))
                target = res.scalars().first()
            if target is None:
                return False
            return True

    async def email_exists(self, email: str) -> bool:
        '''
        Returns `True` if the email already exists
        '''

        if NO_DB:

            for user in fake_users:
                if user.email == email:
                    return True
            return False

        else:
            # TODO: check
            if not checkers.users.check_email_format(email):
                return False
            async with con.begin():
                res= await con.execute(select(User).where(User.email==email))
                target = res.scalars().first()
            if target is None:
                return False
            return True

    async def delete(self, username: str) -> bool:
        '''
        Returns `True` if the username was successfully deleted
        '''
        # TODO: implement


class User(BaseModel):

    async def edit_user_info(new_info: dict) -> bool:
        """
        Edits self using the new user
        """


