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
        verify_email_error.status_code: verify_email_error.response_doc(),
    },
)
async def verify_email(email: str) -> bool:
    if await us.send_verification_email:
        code = status.HTTP_200_OK
    else:
        code = status.HTTP_400_BAD_REQUEST

    return email, code



register_error = JSONError(status.HTTP_400_BAD_REQUEST, '[field] already exists')
@router.post('/register',
    status_code=201,
    description='Successful registration. Returns the username, email, and user_type of the newly-created account.',
    response_model=RegistrationResponse,
    responses={
        register_error.status_code: register_error.response_doc(),
    }
)
async def register(details: RegistrationRequest):
    print(details)
    response = await us.create_user(
        details.username,
        details.email,
        details.password,
        details.user_type,
        details.verification_code
    )
    if response != 'ok':
        return {
            'description': f'{response} already exists'
        }, status.HTTP_400_BAD_REQUEST

    return RegistrationResponse(
        details.username,
        details.email,
        details.user_type,
    )




@router.post(
    '/availability',
    response_model=AvailabilityResponse,
    description='Checks the availability of a username or email. Returns `True` for a field if that field is available, `False` otherwise',    
)
async def availability(fields: AvailabilityRequest):
    print(fields)
    if fields.username:
        fields.username = not await us.username_exists(fields.username)
    if fields.email:
        fields.email = not await us.email_exists(fields.email)
    
    return fields



username_not_found = JSONError(
    status.HTTP_404_NOT_FOUND,
    'Username not found',
)


@router.get('/me',
    responses = {
        unauthorized.status_code: unauthorized.response_doc(),
        forbidden.status_code: forbidden.response_doc(),
        username_not_found.status_code: username_not_found.response_doc(),
    }

)
async def get_me(current_user: User = Depends(get_current_user())):
    #return 'requested info for ' + username + ' as ' + str(current_user)

    return current_user

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