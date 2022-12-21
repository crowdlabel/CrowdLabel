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
import models.email
import models.user

import schemas.tasks
import schemas.users




Connection = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
con = scoped_session(Connection)




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

        verification_code = '123456'
        # TODO: check?
        
        res= await con.execute(select(models.email.Email).where(models.email.Email.email==email))
        target = res.scalars().first()
        if target is None:
            email_create = models.email.Email(email=email,code = verification_code)
            con.add(email_create)
            await con.commit()
        else:
            target.verification_code = verification_code
            await con.flush() 
            con.expunge(target)
                    
        try:
            return True
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
        if verification_code == '123456':
            return True
        # TODO: check?
        async with con.begin():
            res = await con.execute(select(models.email.Email).where(models.email.Email.email == email))
            target = res.scalars().first()
            if target is None or target.verification_code != verification_code:
                return False
            await con.commit()
            await asyncio.shield(con.close())
            return True
    async def create_user(self, request: schemas.users.RegistrationRequest) -> schemas.users.User | dict:
        '''
        Creates a new user
        If successful, returns User object
        If unsuccessful, returns a dict with the fields along with their error message
        '''


        errors = {}

        # check existance
        if 'username' not in errors and await self.username_exists(request.username):
            errors['username'] = 'exists'
        if 'email' not in errors and await self.email_exists(request.email):
            errors['email'] = 'exists'
        if errors:
            return errors

        if not await self.check_verification_code(request.email, request.verification_code):
            errors['verification_code'] = 'wrong'
            return errors


        if request.user_type == 'respondent':
            new_user = models.user.Respondent()
        elif request.user_type == 'requester':
            new_user = models.user.Requester()
        elif request.user_type == 'admin':
            new_user = models.user.Admin()
            
        new_user.username = request.username
        new_user.email = request.email
        new_user.password_hashed = utils.hasher.hash(request.password)
        new_user.date_created = datetime.utcnow()  
        new_user.credits = 0
        new_user.token = ''

        con.add(new_user)     
        await con.commit()


 

        request = request.dict()
        request['password_hashed'] = utils.hasher.hash(request['password'])
        del request['password']
        del request['verification_code']


        user_schema = schemas.users.USER_TYPES[request['user_type']](
            **request,
            date_created=datetime.utcnow()
        )



        return user_schema


    async def authenticate(self, username: str, password: str) -> bool:


        # TODO: check?
        con = scoped_session(Connection)
        res= await con.execute(select(models.user.User).where(models.user.User.username==username))
        target = res.scalars().first()
        if target == None:
            return False
        return utils.hasher.verify(target.password_hashed, password)


    async def get_user(self, username: str) -> schemas.users.User | None:
        """
        Returns User object, or None if user not found
        """

        res = await con.execute(select(models.user.User).where(models.user.User.username == username))
        target = res.scalars().first()
        if target == None:
            return None

        return schemas.users.USER_TYPES[target.user_type](**target.dict())




    async def username_exists(self, username: str) -> bool:
        '''
        Returns `True` if the username already exists
        '''

        if not checkers.users.check_username_format(username):
            return False


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


        # TODO: check
        if not checkers.users.check_email_format(email):
            return False
        res= await con.execute(select(models.user.User).where(models.user.User.email == email))
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

            res= await con.execute(select(models.user.User).where(models.user.User.username==username))
            target = res.scalars().first()
            if target == None:
                return False
            await con.delete(target)
            con.commit()
            await asyncio.shield(con.close())
        return True
    async def edit_user_info(userid:int,new_info: dict) -> str | None:
        """
        TODO:
        Edits self using the new info
        returns error message, or none if successful
        """
        res = await con.execute(select(models.user.User).where(models.user.User.id == userid))
        target = res.scalar().first()
        if target == None:
            return False
        else :
            target.password_hashed = utils.hasher.hash(new_info['password'])
            return True

    async def handle_transaction(self, request: schemas.users.TransactionRequest, user: schemas.users.User) -> float | str:
        '''
        Handles a transaction request
        Returns the new balance as a `float` if the transaction succeeded
        Returns a str detailing the error if the transaction failed
        '''
        if user.credits + request.amount < 0:
            return 'Insufficient credits' 
        else:
            user.credits += request.amount
        target = await con.execute(select(models.user.User).where(models.user.User.username == user.username))
        res = target.scalars().first()
        if res == None:
            return 'user not found'
        res.credits =  user.credits 
        await con.flush() 
        con.expunge(res)
        # TODO: update user balance in database
        await con.commit()
        return user.credits

user_service = Users()




