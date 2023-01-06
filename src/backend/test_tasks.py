from test_utils import *
from test_data import req1, res1, res2, example_task, expected_task

def test_upload():
    init_models_sync()
    register(req1)
    token = login(req1)
    top_up(token, 1000)

    file = example_task
    response = upload_task(token, file)
    assert response.status_code == 200
    json = response.json()
    assert 'date_created' in json
    assert time_in_range(json['date_created'])
    assert 'task_id' in json
    assert 'tags' in json

    compare_dicts(expected_task, json)

    response = get_me(token)
    assert response.status_code == 200
    assert json['task_id'] in response.json()['tasks_requested']



def test_search():
    init_models_sync()
    register(req1)
    token = login(req1)
    credits(token, 100)
    task1 = upload_task(token, example_task)
    register(res1)
    jd = login(res1)
    response = client.put('/tasks/', headers=jd, json={})
    assert response.status_code == 200
    json = response.json()
    assert 'tasks' in json and 'total' in json
    assert json['total'] == 1 and len(json['tasks']) == 1
    response = client.put('/tasks/', headers=jd, json={'credits_min': 0, 'credits_max': 10})
    assert response.status_code == 200
    json = response.json()
    assert len(json['tasks']) == 1
def test_claim():
    init_models_sync()
    register(res1)
    register(req1)
    reqt = login(req1)
    johnt = login(res1)
    credits(reqt, 100)
    task_id = upload_task(reqt, example_task).json()['task_id']
    cresp = claim(johnt, task_id)
    assert cresp.status_code == 200
    assert res1['username'] in get_task(reqt, task_id).json()['respondents_claimed']
    assert task_id in get_me(johnt).json()['tasks_claimed']

def test_get_task():
    init_models_sync()
    register(req1)
    token = login(req1)
    credits(token, 100)
    credits(token, 100)
    task = upload_task(token, example_task).json()
    response = get_task(token, task['task_id'])
    assert response.status_code == 200
    json = response.json()
    compare_dicts(task, json)
def test_get_task_question_resource():
    init_models_sync()
    register(req1)
    token = login(req1)
    credits(token, 100)
    task_id = upload_task(token, example_task).json()['task_id']
    response = get_task_question_resource(token, task_id, 2)
    assert response.status_code == 200
    assert response.status_code == 200
    content = response.content
    with open('../../examples/example_task/camouflage.jpeg', 'rb') as f:
        original = f.read()
    assert content == original
def test_answer():

    init_models_sync()
    register(res1)
    register(req1)
    reqt = login(req1)
    johnt = login(res1)
    credits(reqt, 100)
    task_id = upload_task(reqt, example_task).json()['task_id']
    cresp = claim(johnt, task_id)   
    response = answer(johnt, task_id, 1,
        {'choice': 1}
    )
    assert response.status_code == 200

    task = get_task(reqt, task_id).json()
    print('#'*100)
    for question in task['questions']:
        if question['question_id'] == 1:
            assert question['answers'] == [{'choice': 1}]
            break

def test_get_cover():
    init_models_sync()
    register(res1)
    register(req1)
    reqt = login(req1)
    credits(reqt, 100)
    task_id = upload_task(reqt, example_task).json()['task_id']
    response = get_cover(reqt, task_id)
    assert response.status_code == 200
    with open('../../examples/example_task/cover.jpg', 'rb') as f:
        assert f.read() == response.content

def test_answer_type():
    init_models_sync()
    register(req1)
    register(res1)
    req1t = login(req1)
    res1t = login(res1)
    top_up(req1t, 1000)
    task_id = upload_task(req1t, example_task).json()['task_id']
    claim(res1t, task_id)
    response = answer(res1t, task_id, 1, {'choices': [0, 1]})
    assert response.status_code == 400
    print(response.json())

""" def test_answer_visibility():
    init_models_sync()
    register(req1)
    register(res1)
    register(res2)
    req1t = login(req1)
    res1t = login(res1)
    res2t = login(res2)
    top_up(req1t, 1000)
    task_id = upload_task(req1t, example_task).json()['task_id']
    claim(res1t, task_id)
    claim(res2t, task_id)
    answer(res1t, task_id, 1, {'choice': 0})
    answer(res1t, task_id, 5, {'choice': 0})
    answer(res2t, task_id, 1, {'choice': 1})
    answer(res2t, task_id, 5, {'choice': 1})
    task1 = get_task(res1t, task_id).json()
    task2 = get_task(res2t, task_id).json()
    for question in task1['questions']:
        assert len(question['answers']) == 1
        assert question['answers'][0]['respondent'] == res1['username']
    #pprint(task1)
    #pprint(task2) """

def test_answer_visibility():
    init_models_sync()
    register(req1)
    register(res1)
    register(res2)
    req1t = login(req1)
    res1t = login(res1)
    res2t = login(res2)
    top_up(req1t, 1000)
    task_id = upload_task(req1t, example_task).json()['task_id']
    claim(res1t, task_id)
    claim(res2t, task_id)
    answer(res1t, task_id, 1, {'choices': [0]})
    answer(res1t, task_id, 5, {'choices': [0]})
    answer(res2t, task_id, 1, {'choices': [1]})
    answer(res2t, task_id, 5, {'choices': [1]})
    task1 = get_task(res1t, task_id).json()
    for question in task1['questions']:
        assert len(question['answers']) <= 1
        if len(question['answers']) == 1:
            assert question['answers'][0]['respondent'] == res1['username']
    questions = [get_question(res1t, task_id, i).json() for i in (1, 5)]
    for question in questions:
        assert len(question['answers']) <= 1
        if len(question['answers']) == 1:
            assert question['answers'][0]['respondent'] == res1['username']