from fastapi.testclient import TestClient

from main import app, init_models_sync
from datetime import datetime
from pathlib import Path

client = TestClient(app)


admin = {
    'username': 'admin',
    'email': 'admin@example.com',
    'password': 'secret123',
    'user_type': 'admin',
    'verification_code': '123456',
}

johndoe = {
    'username': 'johndoe',
    'email': 'johndoe@example.com',
    'password': 'secret123',
    'user_type': 'respondent',
    'verification_code': '123456',
}

req = {
    'username': 'req1',
    'email': 'req1@gmail.com',
    'password': 'requester123',
    'user_type': 'requester',
    'verification_code': '123456'
}

def __register(user):
    response = client.post('/users/register', json=user)
    assert response.status_code == 201

def __login(user):
    # TODO
    response = client.post('/login', data={
        'username': user['username'],
        'password': user['password']
    })
    token = {'Authorization': f'Bearer {response.json()["access_token"]}'}
    return token

def __top_up(token, amount):
    response = client.post('/users/me/balance',
        headers=token,
        json={'amount': amount}
    )
    assert response.status_code == 200

def __get_me(token):
    return client.get('/users/me/', headers=token)

def test_get_me():
    init_models_sync()
    __register(req)
    token = __login(req)
    response = __get_me(token)
    assert response.status_code == 200
    for field in ['username', 'email', 'user_type']:
        assert req[field] == response.json()[field]



def test_register():
    init_models_sync()
    now = datetime.utcnow()
    response = client.post('/users/register', json=admin)
    assert response.status_code == 201
    json = response.json()
    assert 'date_created' in json
    date_created = datetime.strptime(json['date_created'], '%Y-%m-%dT%H:%M:%S.%f')
    assert abs((now - date_created).total_seconds()) < 5 # a few seconds buffer for request round trip
    del json['date_created'] # remove date_created from equality check
    success_expected = {
        'username': 'admin',
        'email': 'admin@example.com',
        'user_type': 'requester',
        'credits': 0,
        'tested': False,
        'tasks_claimed': [],
        'tasks_completed': [],
        'tasks_requested': []
    }
    assert json == success_expected


def test_availability():
    init_models_sync()

    response = client.put('/users/availability',
        json={
            'username': 'johndoe',
            'email': 'johndoe@example.com',
        }
    )


def test_upload():
    init_models_sync()
    __register(req)
    token = __login(req)
    print(__get_me(token).json())
    __top_up(token, 100)
    print(__get_me(token).json())
    file = Path('D:/example_task.zip').absolute()
    files = {'task_file': (file.name, open(file, 'rb'))}
    response = client.post('/tasks/upload',
        headers=token,
        files=files
    )

    print(response.status_code, response.json())



from schemas.tasks import TaskSearchRequest
from services.tasks import Tasks

if __name__ == '__main__':
    test_upload()