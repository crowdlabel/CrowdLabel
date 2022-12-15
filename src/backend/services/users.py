import checkers.users
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
import utils.hasher
import utils.emailsender
from sqlalchemy import select, update
import random
from services.database import *
from datetime import datetime
from pydantic import BaseModel
import services.tasks
import models.email
import models.user



Connection = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
con = scoped_session(Connection)

task_service = services.tasks.Tasks()

class User(BaseModel):
    username: str=''
    email: str=''
    user_type: str=''
    credits: float=0
    date_created: datetime=datetime.utcnow()
    password_hashed: str=''

    async def edit_user_info(new_info: dict) -> bool:
        """
        Edits self using the new user
        """

    class Config:
        schema_extra = {
            'example': {
                'username': 'johndoe',
                'email': 'johndoe@example.com',
                'user_type': 'respondent',
                'credits': 0,
                'date_created': datetime(1970, 1, 1, 0, 0 , 0),
                'tested': False,
                'tasks_claimed': {1, 4},
                'tasks_completed': {2, 3},
            }
        }

class Requester(User):
    user_type='requester'
    tasks_requested: set[int]=set() # list Task IDs
class Respondent(User):
    user_type='respondent'
    tested: bool=False
    tasks_claimed: set[int]=set() # list Task IDs
    tasks_completed: set[int]=set() # list Task IDs

    async def claim_task(self, task: services.tasks.Task | int) -> str | None:
        if isinstance(task, int):
            task = await task_service.get_task(task)
        self.tasks_claimed.add(task.task_id)
        task.respondents_claimed.add(self.username)
        return task
        # TODO: claim task
        # returns error message, or none if successful

class Admin(Requester, Respondent):
    pass

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


        # TODO: check?
        async with con.begin():
            res= await con.execute(select(models.email.Email).where(models.email.Email.email==email))
            target = res.scalars().first()
            if target is None:
                email_create = models.email.Email(email=email,code = verification_code)
                con.add(email_create)
                await con.commit()
            else:
                print(f'update code from {target.verification_code} to {verification_code}')
                target.verification_code = verification_code
                await con.flush()
                con.expunge(target)
                    
        try:
            self.__email_sender.send_email(
                'CrowdLabel 邮箱验证码',
                verification_code,
                'noreply@crowdlabel.org',
                [email]
            )
            return True
        except:
            return False


    async def check_verification_code(self, email: str, verification_code: str):

        # TODO: check?
        async with con.begin():
            res= await con.execute(select(models.email.Email).where(models.email.Email.email==email))
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
        del args['self']


        errors = {}

        # check arguments' formats
        for arg in args:
            if arg  == 'self':
                continue
            # if not checkers.users.format_checkers[arg](args[arg]):
            #     errors[arg] = 'format'

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

        if user_type in ['0', 'respondent']:
            new_user = Respondent()
            new_user.user_type = 'respondent'

        elif user_type in ['1', 'requester']:
            new_user = Requester()
            new_user.user_type = 'requester'
        new_user.username = username
        new_user.email = email
        new_user.password_hashed = utils.hasher.hash(password)
        new_user.date_created = datetime.utcnow()       
        con.add(new_user)     
        await con.commit()
        return new_user


    async def authenticate(self, username: str, password: str) -> bool:


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

        # TODO: check
        if not checkers.users.check_username_format(username):
            return False
        async with con.begin():
            res= await con.execute(select(models.user.User).where(models.user.User.username==username))
            target = res.scalars().first()
        if target is None:
            return False
        return True

    async def email_exists(self, email: str) -> bool:
        '''
        Returns `True` if the email already exists
        '''

        # TODO: check
        if not checkers.users.check_email_format(email):
            return False
        async with con.begin():
            res= await con.execute(select(models.user.User).where(models.user.User.email==email))
            target = res.scalars().first()
        if target is None:
            return False
        return True

    async def delete(self, username: str) -> bool:
        '''
        Returns `True` if the username was successfully deleted
        '''
        # TODO: implement
        async with con.begin():

            res= await con.execute(select(User).where(User.username==username))
            target = res.scalars().first()
            if target == None:
                return False
            await con.delete(target)
            con.commit()
        return True
    async def edit_user_info(userid:int,new_info: dict) -> str | None:
        """
        TODO:
        Edits self using the new info
        returns error message, or none if successful
        """
        async with con.begin():
            res = await con.execute(select(User).where(User.id == userid))
            target = res.scalar().first()
            if target == None:
                return False
            else :
                target.password_hashed = utils.hasher.hash(new_info['password'])
                return True

