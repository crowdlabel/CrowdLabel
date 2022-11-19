from .base import *
import services.user
from .login_required import login_required
from fastapi import Response
from fastapi.responses import JSONResponse
from .schemas import *
from services.user import username_exists, email_exists, send_verification_email

@app.post('/verify_email',

)
async def verify_email(email: Email):
    """
    Sends a verification email
    Returns 
    """
    return await send_verification_email(email)






@app.post('/register',
    #response_model=JWT,
    status_code=201,
    description='Successful registration. Returns the username, email, and user_type of the newly-created account.',
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