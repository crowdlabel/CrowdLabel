from flask import request, Blueprint
from user import *
from flask_restful import Resource


api = Blueprint('api', __name__)


API_VERSION = 1



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
    if correct_credentials(username, password):
        # TODO: return JWT
        return True
    else:
        return False

@api.route(f'/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if username_exists(username):
        login_message = "温馨提示：用户已存在，请直接登录"
        return
    else:
        create_user(
            username,
            request.form['email'],
            password,
            0
        )



@api.route('/user/<username>')
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