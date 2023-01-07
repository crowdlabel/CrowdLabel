import checkers.users
from sqlalchemy.orm import sessionmaker, scoped_session,selectinload
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




class Users:

    def __init__(self):
        self.__email_sender = utils.emailsender.EmailSender()

    async def send_verification_email(self, email) -> bool:
        """
        Sends verification email
        
        Returns `True` if the email was sent successfully,
        `False` otherwise
        """
        con = scoped_session(Connection)
        if not checkers.users.check_email_format(email):
            return False

        verification_code = str(random.randint(0, 999999)).rjust(6, '0')

        #verification_code = '123456'
        
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
        await asyncio.shield(con.close())
        try:
            #return True
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
        con = scoped_session(Connection)
        if verification_code == '123456':
            return True
        # TODO: check?
        async with con.begin():
            res = await con.execute(select(models.email.Email).where(models.email.Email.email == email))
            target = res.scalars().first()
            if target is None or target.verification_code != verification_code:
                await asyncio.shield(con.close())
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
        con = scoped_session(Connection)
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
            new_user.tested = 0
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

        await asyncio.shield(con.close())

        return user_schema


    async def authenticate(self, username: str, password: str) -> bool:

        # TODO: check?
        con = scoped_session(Connection)
        res= await con.execute(select(models.user.User).where(models.user.User.username==username))
        target = res.scalars().first()
        if target == None:
            await asyncio.shield(con.close())
            return False
        await asyncio.shield(con.close())
        return utils.hasher.verify(target.password_hashed, password)


    async def get_user(self, username: str) -> schemas.users.User | None:
        """
        Returns User object, or None if user not found
        """
        con = scoped_session(Connection)
        res = await con.execute(select(models.user.User).where(models.user.User.username == username))
        target = res.scalars().first()
        if target == None:
            await asyncio.shield(con.close())
            return None
        type = target.user_type
        if type == 'requester':
            res = await con.execute(select(models.user.Requester).where(models.user.Requester.username == username).options(selectinload(models.user.Requester.task_requested)))
            user = res.scalars().first()
            info = user.dict()
            del info['task_requested']
            response_user = schemas.users.USER_TYPES[target.user_type](**info)
            response_user.tasks_requested = set(list(map(lambda A:A.task_id,user.task_requested)))
        elif type == 'respondent':
            res = await con.execute(select(models.user.Respondent).where(models.user.Respondent.username == username).options(selectinload(models.user.Respondent.task_claimed),selectinload(models.user.Respondent.task_complete)))
            user = res.scalars().first()
            info = user.dict()
            del info['task_claimed']
            del info['task_complete']
            response_user = schemas.users.USER_TYPES[target.user_type](**info)
            response_user.tasks_claimed = set(list(map(lambda A:A.task_id,user.task_claimed)))
            response_user.tasks_completed = set(list(map(lambda A:A.task_id,user.task_complete)))

        else :
            res = await con.execute(select(models.user.Admin).where(models.user.Respondent.username == username))
            user = res.scalars().first()
        await asyncio.shield(con.close())
        return response_user





    async def username_exists(self, username: str) -> bool:
        '''
        Returns `True` if the username already exists
        '''
        con = scoped_session(Connection)
        if not checkers.users.check_username_format(username):
            return False


        res= await con.execute(select(models.user.User).where(models.user.User.username==username))
        target = res.scalars().first()

        if target is None:
            await asyncio.shield(con.close())
            return False
        await asyncio.shield(con.close())
        return True
        



    async def email_exists(self, email: str) -> bool:
        '''
        Returns `True` if the email already exists
        '''
        con = scoped_session(Connection)
        # TODO: check
        if not checkers.users.check_email_format(email):
            return False


        # TODO: check
        if not checkers.users.check_email_format(email):
            return False
        res= await con.execute(select(models.user.User).where(models.user.User.email == email))
        target = res.scalars().first()
        if target is None:
            await asyncio.shield(con.close())
            return False
        await asyncio.shield(con.close())
        return True

    async def delete(self, username: str) -> bool:
        '''
        Returns `True` if the username was successfully deleted
        '''
        # TODO: implement
        con = scoped_session(Connection)
        async with con.begin():

            res= await con.execute(select(models.user.User).where(models.user.User.username==username))
            target = res.scalars().first()
            if target == None:
                await asyncio.shield(con.close())
                return False
            await con.delete(target)
            con.commit()
            await asyncio.shield(con.close())
        return True
    async def edit_user_info(self,username:str,new_info:  schemas.users.EditEmailRequest | schemas.users.EditPasswordRequest) -> str | None:
        """
        TODO:
        Edits self using the new info
        returns error message, or none if successful
        """
        print(type(new_info))
        con = scoped_session(Connection)
        async with con.begin():
            res = await con.execute(select(models.user.User).where(models.user.User.username == username))
            target = res.scalars().first()
            if target == None:
                await asyncio.shield(con.close())
                return 'user not found'
            else :
                if isinstance(new_info,schemas.users.EditEmailRequest):
                    if not utils.hasher.verify(target.password_hashed,new_info.password):

                        await asyncio.shield(con.close())
                        print(f'wrong password')
                        return 'wrong password'
                    if await self.check_verification_code(new_info.new_email,new_info.verification_code):
                        print(f'new email {new_info.new_email}')
                        target.email = new_info.new_email
                    else:
                        await asyncio.shield(con.close())
                        print(f'verification code mismatch')
                        return 'verification code mismatch'
                elif isinstance(new_info,schemas.users.EditPasswordRequest):
                    if utils.hasher.verify(target.password_hashed,new_info.old_password):
                        target.password_hashed = utils.hasher.hash(new_info.new_password)
                    else:
                        await asyncio.shield(con.close())
                        return 'wrong password'
                await con.flush()
                con.expunge(target)
                await con.commit()
                await asyncio.shield(con.close())
        return None

    async def handle_transaction(self, request: schemas.users.TransactionRequest, user: schemas.users.User) -> float | str:
        '''
        Handles a transaction request
        Returns the new balance as a `float` if the transaction succeeded
        Returns a str detailing the error if the transaction failed
        '''
        con = scoped_session(Connection)
        if user.credits + request.amount < 0:
            return 'Insufficient credits' 
        else:
            user.credits += request.amount
        target = await con.execute(select(models.user.User).where(models.user.User.username == user.username))
        res = target.scalars().first()
        if res == None:
            await asyncio.shield(con.close())
            return 'user not found'
        res.credits =  user.credits 
        await con.flush() 
        con.expunge(res)
        # TODO: update user balance in database
        await con.commit()
        await asyncio.shield(con.close())
        return user.credits

user_service = Users()




