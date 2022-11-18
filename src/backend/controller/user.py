from .base import *
import services.user
from .login_required import login_required
from utils.emailverification import send_verification_email
from fastapi import Response
from fastapi.responses import JSONResponse
from .schemas import *
from services.user import username_exists, email_exists

API_VERSION = 1

@app.post('/login',
    response_model=JWT,
    status_code=200,
    description='Successful login. Returns the `jwt` associated with the provided credentials.',
    responses = {
        login_error.status_code: login_error.response_doc()
    }
)
async def login(credentials: Credentials):

    jwt = await services.user.login(credentials.username, credentials.password)

    if not jwt:
        return login_error.response()

    return {'jwt': jwt}




@app.post('/register',
    #response_model=JWT,
    status_code=201,
    description='Successful registration. Returns the `jwt` associated with the newly-created account',
    responses = {
        login_error.status_code: login_error.response_doc()
    }
)
async def register(details: Registration):
    # TODO: 
    print(details)
    response = services.user.create_user(
        details.username,
        details.email,
        details.password,
        details.user_type)
    if response != 'ok':
        return {
            'error': f'{response} already exists'
        }, 400

    
    else:
        return {
            'username': details.username,
            'email': details.email,
            'user_type': details.user_type,
        }, 200



@app.post('/availability', response_model=Availability)
async def availability(fields: Availability):
    availability = Availability()
    try:
        availability.username = username_exists(fields.username)
    except:
        availability.username = False
    try:
        availability.email = email_exists(fields.email)
    except:
        availability.email = False
    
    return availability


@app.get('/user/<username>')
@login_required
async def user(username):
    return 'requested info for ' + username