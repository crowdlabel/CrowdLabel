from .base import app
from utils.filetransfer import *
from fastapi import APIRouter

task_router = APIRouter(prefix='/task')

@app.get('/tasks')
async def tasks():
    return 'api: tasks'

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
