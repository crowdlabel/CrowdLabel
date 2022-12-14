from utils.hasher import hash
from datetime import datetime

from schemas.users import Requester, Respondent, Admin
from schemas.tasks import Task
from schemas.questions import *

fake_users = [
    Respondent(
        username='johndoe',
        email='johndoe@example.com',
        password_hashed=hash('secret'),
        date_created=datetime(2022, 10, 9, 10, 10),
        credits=0,
        tested=True,
        tasks_claimed=[],
        tasks_completed=[]
    ),
    Requester(
        username='requester1',
        email='requester1@example.com',
        password_hashed=hash('secret'),
        date_created=datetime(2022, 10, 9, 10, 10),
        credits=0,
        tasks_requested=[1],
    ),
    Admin(
        username='admin',
        email='admin@example.com',
        password_hashed=hash('secret'),
        date_created=datetime(2022, 10, 10, 10, 10, 10),
        credits=0,
        tasks_requested=[],
    )
]

fake_emails = {
    'me@georgetian.com': '000000'
}

fake_tasks = [
    Task(
        task_id=1,
        name='faketask',
        creator='requester1',
        responses_required=10,
        date_created=datetime.utcnow(),
        credits=10,
        questions=[
            SingleChoiceQuestion(
                task_id=1,
                question_id=1,
                prompt='Which number is a prime number?',
                options=['9', '10', '11', '12'],
                answers=[],
            ),
        ]
    ),
]

