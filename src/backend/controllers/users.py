from fastapi import status
from fastapi.routing import APIRouter
from .auth import User, Depends, get_current_user
from .jsondocumentedresponse import JSONDocumentedResponse, create_documentation
import services.users
import schemas.users


router = APIRouter()
user_service = services.users.Users()
###############################################################################
availability_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'The availability of the requested fields.',
    schemas.users.AvailabilityResponse,
)
@router.put('/availability',
    description='Checks the availability of a username or email. Returns `true` for a field if that field is available, `false` otherwise.',
    **create_documentation([availability_jdr])
)
async def availability(fields: schemas.users.AvailabilityRequest):
    print(fields)
    response = schemas.users.AvailabilityResponse()
    if fields.username:
        response.username = not await user_service.username_exists(fields.username)
    if fields.email:
        response.email = not await user_service.email_exists(fields.email)
    print(response)
    return availability_jdr.response(response)
###############################################################################
verify_email_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Email sent successfully.',
    schemas.users.Email,
)
verify_email_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Email not sent successfully.',
    schemas.users.Email,
)
@router.post('/verify-email',
    description='Attempts to send an email containing a verification code to the provided address.',
    **create_documentation([verify_email_success_jdr, verify_email_failed_jdr])
)
async def verify_email(email: schemas.users.Email):
    if not await user_service.send_verification_email(email.email):
        return verify_email_failed_jdr.response(email)
    return verify_email_success_jdr.response(email)
###############################################################################
register_success_jdr = JSONDocumentedResponse(
    status.HTTP_201_CREATED,
    'Account successfully created. Returns all the following fields:',
    schemas.users.User
)
register_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Account creation failed. The field(s) that caused the failure and its corresponding error (`exists` for existing field (`username` or `email`), `format` (any field), or `wrong` (`verification_code`) is returned. Not all fields will necessarily be present.',
    schemas.users.RegistrationError
)
@router.post('/register', 
    description='Register for an account. To be called after obtaining a verification code by calling `/verify-email`.',
    **create_documentation([register_success_jdr, register_failed_jdr])
)
async def register(details: schemas.users.RegistrationRequest):
    response = await user_service.create_user(**details)

    if response:
        response = schemas.users.RegistrationError(**response)
        return register_failed_jdr.response(response)



    return response# register_success_jdr.response(response)
###############################################################################
me_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Successfully got me',
    schemas.users.User
)
@router.get('/me',
    description='Gets information for user who sent the request',
    **create_documentation([me_jdr])
)
async def get_me(current_user: User = Depends(get_current_user())):
    return me_jdr.response(current_user, {'password_hashed'})
###############################################################################
@router.patch('/me',
    description='Updates user info'
)
async def edit_me(current_user: User = Depends(get_current_user())):
    # edit user's own details
    # TODO
    pass
###############################################################################
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
    user = user_service.get_user(username)
    if not user:
        return username_failed_jdr.response()
    return user

