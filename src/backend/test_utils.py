from pprint import pprint
from fastapi.testclient import TestClient
from controllers.routers import app
from datetime import datetime
from services.database import init_models_sync
client = TestClient(app)

def get_cover(token, task_id):
    return client.get(f'/tasks/{task_id}/cover-image', headers=token)

def availability(username=None, email=None):
    request = {}
    if username:
        request['username'] = username
    if email:
        request['email'] = email
    return client.put('/users/availability', json=request)
def register(user):
    return client.post('/users/register', json=user)
def login(user, format=True):
    response = client.post('/login', data={
        'username': user['username'],
        'password': user['password']
    })
    if format:
        return {'Authorization': f'Bearer {response.json()["access_token"]}'}
    return response

def top_up(token, amount):
    return client.post('/users/me/credits',
        headers=token,
        json={'amount': amount}
    )
def get_me(token):
    return client.get('/users/me/', headers=token)
def edit_me(token, data):
    return client.put('/users/me', json=data)

def upload_task(token, file):
    files = {'task_file': (file.name, open(file, 'rb'))}
    response = client.post('/tasks/upload',
        headers=token,
        files=files
    )
    return response
def claim(token, task_id):
    return client.post(f'/tasks/{task_id}/claim', headers=token)
def get_task(token, task_id):
    return client.get(f'/tasks/{task_id}', headers=token)
def credits(token, amount):
    return client.post('/users/me/credits', headers=token, json={'amount': amount})
def get_task_question_resource(token, task_id, question_id):
    return client.get(f'/tasks/{task_id}/questions/{question_id}/resource', headers=token)
def answer(token, task_id, question_id, answer):
    return client.put(f'/tasks/{task_id}/questions/{question_id}/answer', headers=token, json=answer)
def get_cover(token, task_id):
    return client.get(f'/tasks{task_id}/cover-image', headers=token)
def time_in_range(time, range=5):
    if isinstance(time, str):
        time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f')
    return abs((datetime.utcnow() - time).total_seconds()) < range

def compare_dicts(t1: dict, t2: dict,
    exclude = {
        'date_created',
    },
    sets = {
        'respondents_claimed',
        'respondents_completed',
        'tags'
    }
) -> bool:
    keys = set(t1.keys()) + set(t2.keys())
    for key in keys:
        if key in exclude:
            continue
        if key in sets:
            if set(t1[key]) != set(t2[key]):
                return False
        if t1[key] != t2[key]:
            return False
    return True
