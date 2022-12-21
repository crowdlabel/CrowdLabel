from fastapi.testclient import TestClient
from pprint import pprint
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

example_task = Path('D:/example_task.zip')

def __register(user):
    return client.post('/users/register', json=user)

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

def __upload_task(token, file):
    files = {'task_file': (file.name, open(file, 'rb'))}
    response = client.post('/tasks/upload',
        headers=token,
        files=files
    )
    return response

def __claim(token, task_id):
    response = client.post(f'/tasks/{task_id}/claim', headers=token)
    return response

def __get_task(token, task_id):
    return client.get(f'/tasks/{task_id}', headers=token)

def test_get_me():
    init_models_sync()
    __register(req)
    token = __login(req)
    response = __get_me(token)
    assert response.status_code == 200
    for field in ['username', 'email', 'user_type']:
        assert req[field] == response.json()[field]
    print(response.json())

def time_in_range(time, buffer=5):
    if isinstance(time, str):
        time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f')
    return abs((datetime.utcnow() - time).total_seconds()) < buffer

def test_register():
    init_models_sync()
    now = datetime.utcnow()
    response = __register(admin)
    assert response.status_code == 201
    json = response.json()
    assert 'date_created' in json
    assert time_in_range(json['date_created'])
    del json['date_created'] # remove date_created from equality check
    expected = {
        'username': 'admin',
        'email': 'admin@example.com',
        'user_type': 'admin',
        'credits': 0,
        'tested': False,
        'tasks_claimed': [],
        'tasks_completed': [],
        'tasks_requested': []
    }
    pprint(json)
    pprint(expected)
    assert json == expected


def test_availability():
    init_models_sync()

    response = client.put('/users/availability',
        json={
            'username': 'kennyl',
            'email': 'johndoe@example.com',
        }
    )

    print(response.json())


def test_upload():
    init_models_sync()
    __register(req)
    token = __login(req)
    __top_up(token, 100)
    file = example_task
    response = __upload_task(token, file)
    print(response.status_code)
    assert response.status_code == 200
    expected = {
        'cover_image': 'cover.jpg',
        'credits': 2.0,
        'description': 'This task is an example of a valid task',
        'introduction': 'This is an example',
        'name': 'Example task',
        'questions': [{'answers': [],
                        'prompt': 'What sentiment does this text convey',
                        'question_id': 1,
                        'question_type': 'single_choice',
                        'resource': 'text.txt'},
                    {'answers': [],
                        'prompt': 'Draw a box around the person in this image',
                        'question_id': 2,
                        'question_type': 'bounding_box',
                        'resource': 'camouflage.jpeg'},
                    {'answers': [],
                        'prompt': 'Transcribe the following audio recording',
                        'question_id': 3,
                        'question_type': 'open',
                        'resource': 'armstrong.mp3'},
                    {'answers': [],
                        'prompt': 'What objects are present in the following image',
                        'question_id': 4,
                        'question_type': 'multi_choice',
                        'resource': 'nature.jpg'}],
        'requester': 'req1',
        'respondents_claimed': [],
        'respondents_completed': [],
        'responses_required': 2,
        'tags': ['object-bounding',
                'audio-transcription',
                'object-detection',
                'sentiment-analysis'],
    }
    json = response.json()
    assert 'date_created' in json
    assert time_in_range(json['date_created'])
    assert 'task_id' in json
    assert 'tags' in json
    assert set(json['tags']) == set(expected['tags'])
    assert 'resource_path' in json
    for key in ['resource_path', 'tags', 'task_id', 'date_created']:
        del json[key]
    del expected['tags']


    assert json == expected

    #response = __upload_task(token, file)
    #response = __upload_task(token, file)
    #pprint(json)
    #pprint(expected)


def test_search():
    init_models_sync()
    __register(req)
    token = __login(req)
    task1 = __upload_task(token, example_task)
    __register(johndoe)
    jd = __login(johndoe)
    response = client.put('/tasks/', headers=jd, json={})
    print(response.status_code, response.content)

def test_claim():
    init_models_sync()
    __register(johndoe)
    __register(req)
    reqt = __login(req)
    johnt = __login(johndoe)
    tasku = __upload_task(reqt, example_task).json()
    cresp = __claim(johnt, tasku['task_id'])
    print(cresp.status_code)
    pprint(cresp.json())

    task = __get_task(reqt, tasku['task_id'])
    print(task.status_code)
    pprint(task.json())



    


from schemas.tasks import TaskSearchRequest
from services.tasks import Tasks

if __name__ == '__main__':
    #test_register()
    #test_availability()
    #test_search()
    #test_get_me()
    #test_upload()
    test_claim()