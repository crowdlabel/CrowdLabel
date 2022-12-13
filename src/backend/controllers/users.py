from fastapi import status
from fastapi.routing import APIRouter
from .auth import User, Depends, get_current_user
from .jsonerror import json_response, JSONError, unauthorized, forbidden
import services.users
from schemas.users import AvailabilityRequest, AvailabilityResponse, RegistrationRequest, RegistrationResponse, Email


router = APIRouter()


verify_email_error = JSONError(status.HTTP_400_BAD_REQUEST, 'Email not sent, check email format')
@router.post('/verify-email',
    response_model=Email,
    description='Attempts to send a verification email to the provided address',
    responses={
        status.HTTP_400_BAD_REQUEST: verify_email_error.response_doc(),
    },
)
async def verify_email(email: Email):
    if not await services.users.send_verification_email(email.email):
        return verify_email_error.response()
    return email

register_error = JSONError(status.HTTP_400_BAD_REQUEST, 'Error in one or more fields')
@router.post('/register',
    status_code=status.HTTP_201_CREATED,
    description='NOT FINALIZED Successful registration.',
    response_model=RegistrationResponse,
    responses={
        register_error.status_code: register_error.response_doc(),
    }
)
async def register(details: RegistrationRequest):
    response = await services.users.create_user(
        details.username,
        details.email,
        details.password,
        details.user_type,
        details.verification_code
    )
    if not response:
        response = RegistrationResponse()
        response.username = details.username
        response.email = details.email
        response.user_type = details.user_type

    return response


@router.put(
    '/availability',
    response_model=AvailabilityResponse,
    description='Checks the availability of a username or email. Returns `True` for a field if that field is available, `False` otherwise',    
)
async def availability(fields: AvailabilityRequest):
    print(fields)
    if fields.username:
        fields.username = not await services.users.username_exists(fields.username)
    if fields.email:
        fields.email = not await services.users.email_exists(fields.email)
    
    return fields



username_not_found = JSONError(
    status.HTTP_404_NOT_FOUND,
    'Username not found',
)

@router.get('/me',
    description='Gets information for user who sent the request'
)
async def get_me(current_user: User = Depends(get_current_user())):
    #return 'requested info for ' + username + ' as ' + str(current_user)
    return current_user

@router.patch('/me',
    description='Updates user info'
)
async def edit_me(current_user: User = Depends(get_current_user())):
    # edit user's own details
    # TODO
    pass


@router.get('/{username}',
    responses = {
        unauthorized.status_code: unauthorized.response_doc(),
        forbidden.status_code: forbidden.response_doc(),
        username_not_found.status_code: username_not_found.response_doc(),
    }

)
async def get_user(username: str, current_user: User = Depends(get_current_user(['admin']))):
    #return 'requested info for ' + username + ' as ' + str(current_user)
    user = services.users.get_user(username)
    if not user:
        return json_response(status.HTTP_404_NOT_FOUND, 'Username not found')
    return user

