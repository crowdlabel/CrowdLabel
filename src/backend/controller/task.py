from .base import app
from utils.filetransfer import *
import services.task
from fastapi import APIRouter
from .schemas import *

task_router = APIRouter(prefix='/task')

@app.get('/tasks')
async def tasks():
    return 'api: tasks'

@app.post('/create_task')
async def create_task(details:TaskInfo):
    response = await services.task.create_task(
        details.name,
        details.creator,
        details.details)
    print(response)
    if response != 'ok':
        return {
            'error': f'{response} already exists'
        }, 400

    
    else:
        return {
            'name': details.name,
            'creator': details.creator,
            'details': details.details,
        }, 200
@app.post('/delete_task')
async def delete_task(details:ID):
    response = await services.task.delete_task(details.id)
    if response != 'ok':
        return {
            'error' : f'delete failed'
        },400
@task_router.get('/')
def task(id):
    return 'requested task with id ' + str(id)

@task_router.post(
    '/upload',
)
async def upload_task(in_file: UploadFile, data: str):
    upload_file(in_file, 'upload.test')


@task_router.get(
    '/download',
)
async def download_results():
    return await download_file('main.py')
