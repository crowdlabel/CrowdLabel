import unittest
from src.backend.services.tasks import task_service
from src.backend.services.database import reset_db
import pathlib
import src.backend.schemas.users 
import src.backend.schemas.tasks 
from src.backend.schemas.questions import *
import asyncio
def setup():
    reset_db()
class BasicTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_create_task(self):
        user = src.backend.schemas.users.Requester(
            username='req1',
            email='req1@gmail.com',
            credits=92,
            date_created='2023-01-05 13:39:14.304083',
            password_hashed='$argon2id$v=19$m=65536,t=3,p=4$13B+YNSRYxSPVy11RasdnQ$OMQbX2P5vitjjB43JyWtb6D8POFpAVodNTI5zNJDzTQ',
            tasks_requested=(1,2)
        )
        questions =[
        MultiChoiceQuestion(question_id=1,question_type='multi_choice',prompt='请选择小于5的数字', resource=pathlib.Path('chinese.txt'), answers=[], options=['1', '3', '6', '7']),
        MultiChoiceQuestion(question_id=5, question_type='multi_choice', prompt='请选于3的数字', resource=pathlib.Path('english.txt'), answers=[], options=['1', '4', '6', '8'])
        ]
        task = src.backend.schemas.tasks.CreateTaskRequest(name='Text Multi',credits=2.0,introduction='test',description='text',cover_image='',tags=('文字分类','数字'),responses_required=2,questions=questions)
        path = pathlib.Path('D:\CrowdLabel\src\\backend\data\\tasks\\upload_req1_2023-01-07_10.55.28.141')
        response = await task_service.create_task(user,task,path)
        response.task_id = 0
        expected = src.backend.schemas.tasks.Task(name='Text Multi',credits=2,introduction="test",description="text",cover_image="",tags=('文字分类','数字'),
                                                  responses_required=2,questions=questions,task_id=0,requester='req1',date_created=response.date_created,respondents_claimed=[],
                                                  respondents_completed=[],resource_path=path)
        self.assertEqual(response,expected)
        task.credits = 0
        response = await task_service.create_task(user,task,path)
        self.assertEqual(response,'`credits` must be positive')
        task.credits = 2
        task.responses_required = 0
        response = await task_service.create_task(user,task,path)
        self.assertEqual(response,'`responses_required` must be positive')
        user.credits = 0
        task.responses_required = 2
        response = await task_service.create_task(user,task,path)
        self.assertEqual(response,'Insufficient credits')
        user.credits = 99
        task.tags=('数字',)
        response = await task_service.create_task(user,task,path)
        self.assertEqual(response,'Task without type')
        task.tags=('图片打标','数字')
        response = await task_service.create_task(user,task,path)
        self.assertEqual(response,'Wrong question type')
        task.tags=('文字分类','数字')
        task.questions[0].resource = pathlib.Path('temp.txt')
        response = await task_service.create_task(user,task,path)
        self.assertEqual(response,'The following resources are missing: temp.txt' )
        task.questions[0].resource = pathlib.Path('chinese.txt')
        user.username = 'temp'
        response = await task_service.create_task(user,task,path)
        self.assertEqual(response,'user not found' )
    async def test_claim_task(self):
        username = 'johndoe'
        task_id = 3
        response = await task_service.claim_task(username,task_id)
        
if __name__ == '__main__':
    asyncio.run(unittest.main())