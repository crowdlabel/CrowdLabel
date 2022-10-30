from base import app
from services.user import UserService
from login_required import login_required
from utils.emailverification import send_verification_email

from pydantic import BaseModel

us = UserService()

API_VERSION = 1

class LoginCredentials(BaseModel):
    username: str
    password: str

@app.post('/login')
async def login(credentials: LoginCredentials):

    if us.correct_credentials(
        credentials.username,
        credentials.password):
        # TODO: return JWT, response code success
        return {
            'jwt': ''
        }
    else:
        # TODO: response code fail
        return False


class RegistrationCredentials(BaseModel):
    username: str
    email: str
    password: str
    usertype: int

@app.post('/register')
async def register(credentials: RegistrationCredentials):
    # TODO: 
    response = us.create_user(
        credentials.username,
        credentials.email,
        credentials.password,
        credentials.usertype)
    if response != 'ok':
        return {
            'error': f'{response} already exists'
        }, 400
    else:
        return 200


class Availability(BaseModel):
    username: str | None = None
    email: str | None = None

@app.post('/availability', response_model=Availability)
async def availability(fields: Availability):
    availability = Availability()
    availability.username = 'true'
    availability.email = 'true'
    return availability


@app.get('/user/<username>')
@login_required
async def user(username):
    return 'requested info for ' + username


@app.post('/verify')
def verify():
    username = request.form['username']
    email = request.form['email']
    verification_code = request.form['code']
    verify_email(username, email, verification_code)