from fastapi import status
from fastapi.routing import APIRouter
from .auth import User, Depends, get_current_user
from .jsondocumentedresponse import JSONDocumentedResponse, create_documentation
import services.users
from schemas.users import *


router = APIRouter()

###############################################################################
availability_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'The availability of the requested fields.',
    AvailabilityResponse,
)
@router.put('/availability',
    description='Checks the availability of a username or email. Returns `true` for a field if that field is available, `false` otherwise.',
    **create_documentation([availability_jdr])
)
async def availability(fields: AvailabilityRequest):
    print(fields)
    response = AvailabilityResponse()
    if fields.username:
        response.username = not await services.users.username_exists(fields.username)
    if fields.email:
        response.email = not await services.users.email_exists(fields.email)
    print(response)
    return availability_jdr.response(response)
###############################################################################
verify_email_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Email sent successfully.',
    Email,
)
verify_email_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Email not sent successfully.',
    Email,
)
@router.post('/verify-email',
    description='Attempts to send an email containing a verification code to the provided address.',
    **create_documentation([verify_email_success_jdr, verify_email_failed_jdr])
)
async def verify_email(email: Email):
    if not await services.users.send_verification_email(email.email):
        return verify_email_failed_jdr.response()
    return verify_email_success_jdr.response()
###############################################################################
register_success_jdr = JSONDocumentedResponse(
    status.HTTP_201_CREATED,
    'Account successfully created. Returns all the following fields:',
    GoodRegistrationResponse
)
register_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Account creation failed. The field(s) that caused the failure and its corresponding error (`exists` for existing field (`username` or `email`), `format` (any field), or `wrong` (`verification_code`) is returned. Not all fields will necessarily be present.',
    BadRegistrationResponse
)
@router.post('/register', 
    description='Register for an account. To be called after obtaining a verification code by calling `/verify-email`.',
    **create_documentation([register_success_jdr, register_failed_jdr])
)
async def register(details: RegistrationRequest):
    print('1111111111111111111111111111111')
    response = await services.users.create_user(
        details.username,
        details.email,
        details.password,
        details.user_type,
        details.verification_code,
    )
    print('2222222222222222222222222222')

    if response:
        print('33333333333333333333333')
        response = BadRegistrationResponse(**response)
        return register_failed_jdr.response(response)


    response = GoodRegistrationResponse(
        username=details.username,
        email=details.email,
        user_type=details.user_type,
    )
    return response# register_success_jdr.response(response)


###############################################################################

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



username_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Successfully found user.',
    User
)
username_failed_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'User not found.',
    User
)
@router.get('/{username}',
    description='Gets information for the specified username.',
    **create_documentation([username_success_jdr])
)
async def get_user(username: str, current_user: User = Depends(get_current_user(['admin']))):
    #return 'requested info for ' + username + ' as ' + str(current_user)
    user = services.users.get_user(username)
    if not user:
        return username_failed_jdr.response()
    return user

