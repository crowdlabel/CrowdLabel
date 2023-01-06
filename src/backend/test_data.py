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

example_task = pathlib.Path('D:/bounding.zip')
expected_task = {
    "name": "Bounding box",
    "credits": 2,
    "introduction": "Bounding box",
    "description": "Bounding box",
    "tags": ["图片打标", "人体识别"],
    "responses_required": 2,
    "cover_image": "1.jpg",
    "questions": [
        {
            "question_id": 1,
            "question_type": "bounding_box",
            "prompt": "Draw a box around the person",
            "resource": "2.jpg"
        },
        {
            "question_id": 5,
            "question_type": "bounding_box",
            "prompt": "Draw a box around the person",
            "resource": "3.jpg"
        },
        {
            "question_id": 3,
            "question_type": "bounding_box",
            "prompt": "Draw a box around the person",
            "resource": "1.jpg"
        }
    ]
}