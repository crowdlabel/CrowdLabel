from .base import *
import services.user
from fastapi import Response
from fastapi.responses import JSONResponse
from .schemas import *
from services.user import username_exists, email_exists, send_verification_email
from .auth import User, get_current_active_user, Depends
@app.post('/verify_email',

)
async def verify_email(email: Email):
    """
    Sends a verification email
    Returns 
    """
    return await send_verification_email(email.email)






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


class AvailabilityResponse(BaseModel): 
    username: bool
    email: bool

@app.post('/availability', response_model=AvailabilityResponse)
async def availability(fields: Availability):
    fields.username = True
    fields.email = True
    
    return fields


@app.get('/user/<username>')
async def user(username, current_user: User = Depends(get_current_active_user)):
    return 'requested info for ' + username + ' as ' + str(current_user)
