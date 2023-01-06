from test_utils import *
from test_data import res1, req1


def test_register():
    init_models_sync()
    # regular login
    response = register(req1, format=False)
    assert response.status_code == 201
    response = response.json()
    assert 'date_created' in response
    assert time_in_range(response['date_created'])
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
    assert compare_dicts(response, expected, exclude={'date_created'})
    # duplicate username + duplicate email + wrong verification code
    user = req1.copy()
    user['verification_code'] = '000000'
    response = register(user, format=False)
    assert response.status_code == 400
    response = response.json()
    expected = {
        'username': 'exists', 
        'email': 'exists',
        'verification_code': 'wrong'
    }
    assert response.json() == expected

def test_login():
    init_models_sync()
    # login to non-existent account
    response = login(req1, format=False)
    assert response.status_code == 401
    # login to existing account
    register(req1)
    response = login(req1, format=False)
    assert response.status_code == 200
    assert 'access_token' in response.json()  

def test_availability():
    init_models_sync()
    # query both username and email
    response = availability(req1['username'], req1['email'])
    assert response.status_code == 200
    assert response.json() == {'username': True, 'email': True}
    # query username only
    response = availability(req1['username'])
    assert response.status_code == 200
    assert response.json() == {'username': True}
    # query email only
    response = availability(email=res1['email'])
    assert response.status_code == 200
    assert response.json() == {'email': True}
    # only username is taken
    register(req1)
    response = availability(req1['username'], res1['email'])
    assert response.status_code == 200 and response.json() == {'username': False, 'email': True}
    # username and email both taken
    register(res1)
    response = availability(req1['username'], res1['email'])
    assert response.status_code == 200 and response.json() == {'username': False, 'email': False}

def test_get_me():
    init_models_sync()
    # requester
    register(req1)
    response = get_me(login(req1))
    assert response.status_code == 200
    response = response.json()
    for field in ['username', 'email', 'user_type']:
        assert req1[field] == response[field]
    assert response['tasks_requested'] == []
    assert response['tasks_completed'] == []
    # respondent
    register(res1)
    response = get_me(login(res1))
    for key in ['tasks_claimed', 'tasks_completed']:
        assert key in response.json()

def test_edit_me():
    init_models_sync()
    register(req1)
    token = login(req1)
    # TODO

def test_credits():
    init_models_sync()
    register(johndoe)
    token = login(johndoe)
    assert get_me(token).json()['credits'] == 0

    assert credits(token, -1000).status_code == 400
    assert get_me(token).json()['credits'] == 0

    deposit = 25.4
    assert credits(token, deposit).status_code == 200
    assert get_me(token).json()['credits'] == deposit

    withdraw = -12.7
    assert credits(token, withdraw).status_code == 200
    assert get_me(token).json()['credits'] == deposit + withdraw