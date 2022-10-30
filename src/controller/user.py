from flask import request, Blueprint
from services.user import UserService
from flask_restx import Resource
from login_required import login_required

api = Blueprint('api', __name__)

us = UserService()

API_VERSION = 1


@api.route('/hello')
def hello():
    return {'hello': 'world'}

@api.route(f'/login', methods=['POST'])
def login():
    """
    Accepts credentials in the following dict format:
    {
        'username': '',
        'password': '',
    }
    """

    username = request.form['username']
    password = request.form['password']
    if UserService.correct_credentials(username, password):
        # TODO: return JWT, response code success
        return {
            'jwt': ''
        }
    else:
        # TODO: response code fail
        return False

@api.route('/register', methods=['POST'])
def register():
    # TODO: 
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    usertype = 0
    response = us.create_user(username, email, password, usertype)
    if us.username_exists(username):
        login_message = "温馨提示：用户已存在，请直接登录"
        return
    else:
        us.create_user(
            username,
            request.form['email'],
            password,
            0
        )

@api.route('/availability')
def availability():
    pass


@api.route('/user/<username>')
@login_required
def user(username):
    return 'requested info for ' + username

@api.route('/tasks')
def tasks():
    return 'api: tasks'

@api.route('/task/<id>')
def task(id):
    return 'requested task with id ' + str(id)

@api.route('/verify', methods=['POST'])
def verify():
    username = request.form['username']
    email = request.form['email']
    verification_code = request.form['code']
    verify_email(username, email, verification_code)


@api.route('/admin')
def admin():
    return 'admin'


@api.route('/about')
def about():
    return 'Software Engineering 2022 fall group project'