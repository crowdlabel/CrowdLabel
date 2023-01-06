import pathlib

""" admin = {
    'username': 'admin',
    'email': 'admin@example.com',
    'password': 'secret123',
    'user_type': 'admin',
    'verification_code': '123456',
} """

req1 = {
    'username': 'req1',
    'email': 'req1@gmail.com',
    'password': 'secret123',
    'user_type': 'requester',
    'verification_code': '123456'
}

res1 = {
    'username': 'res1',
    'email': 'resp1@gmail.com',
    'password': 'secret123',
    'user_type': 'respondent',
    'verification_code': '123456'
}

res2 = {
    'username': 'res2',
    'email': 'resp2@gmail.com',
    'password': 'secret123',
    'user_type': 'respondent',
    'verification_code': '123456'
}

example_task = pathlib.Path('D:/text_all.zip')
expected_task = {
    "name": "Text",
    "credits": 2,
    "introduction": "",
    "description": "text",
    "tags": ["文字分类", "语言"],
    "responses_required": 2,
    "questions": [
        {
            "question_id": 1,
            "question_type": "single_choice",
            "prompt": "What language is this?",
            "resource": "chinese.txt",
            "options": ["Chinese", "English"]
        },
        {
            "question_id": 5,
            "question_type": "single_choice",
            "prompt": "What language is this",
            "resource": "english.txt",
            "options": ["Chinese", "English"]
        }
    ]
}