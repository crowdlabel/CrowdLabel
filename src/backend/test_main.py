from fastapi.testclient import TestClient

from main import app, init_models_sync
from datetime import datetime


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



if __name__ == '__main__':
    tests = [
        test_register,
        test_availability,
    ]

    for test in tests:
        test() # run test function