from fastapi import status
from fastapi.routing import APIRouter
from .auth import User, Depends, get_current_user
from .jsonerror import json_response, JSONError, unauthorized, forbidden
import services.user as us
from schemas.users import AvailabilityRequest, AvailabilityResponse, RegistrationRequest, RegistrationResponse

from services.user import send_verification_email


router = APIRouter()


@router.post('/verify-email',

)
async def verify_email(email: str) -> bool:
    """
    Sends a verification email
    Returns `True` if the email sent successfully, `False` otherwise
    """
    return await send_verification_email(email.email)



register_error = JSONError(
    status.HTTP_400_BAD_REQUEST,
    '[field] already exists'
)
@router.post('/register',
    #response_model=JWT,
    status_code=201,
    description='Successful registration. Returns the username, email, and user_type of the newly-created account.',
    response_model=RegistrationResponse,
    responses = {
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
    ), 200




@router.post('/availability', response_model=AvailabilityResponse)
async def availability(fields: AvailabilityRequest):
    fields.username = True
    fields.email = True
    
    return fields



username_not_found = JSONError(
    status.HTTP_404_NOT_FOUND,
    'Username not found',
)

@router.get('/{username}',
    responses = {
        unauthorized.status_code: unauthorized.response_doc(),
        forbidden.status_code: forbidden.response_doc(),
        username_not_found.status_code: username_not_found.response_doc(),
    }

)
async def get_user(username: str, current_user: User = Depends(get_current_user)):
    #return 'requested info for ' + username + ' as ' + str(current_user)
    if current_user.username != username:
        return unauthorized.response()
    user = us.get_user_info(username)
    if not user:
        return json_response(status.HTTP_404_NOT_FOUND, 'Username not found')
