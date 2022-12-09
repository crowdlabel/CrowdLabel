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
        details.type,
        details.details,
        details.introduction,
        details.path)
    if response['status'] != 'ok':
        return {
            'error': f'already exists'
        }, 400

    
    else:
        return {
            'name': details.name,
            'creator': details.creator,
            'details': details.details,
            'introduction':details.introduction,
            'type':details.type,
            'path':details.path
        }, 200
@app.post('/delete_task')
async def delete_task(details:ID):
    response = await services.task.delete_task(details.id)
    if response[0]['status'] != 'ok':
        return {
            'error' : f'delete failed'
        },400
    else :
        return {
            'id':details.id
        },200
@app.post('/edit_task')
async def edit_task(details:TaskDetails):
    response = await services.task.edit_task(
        details.id,
        details.details,
        details.introduction
    )
    if response[0]['status'] != 'ok':
        return {
            'error': 'edit failed'
        },400
    else:
        return {
            'id':response[0]['id'],
            'name':response[0]['name'],
            'creator':response[0]['creator'],
            'details':response[0]['details'],
            'introduction':response[0]['introduction']
        }
@app.post('/get_task')
async def get_task(details:ID):
    response = await services.task.get_task(details.id)
    if response[0]["status"] != "ok":
        return {
            'error' : f'not found id {details.id}'
        },400
    else :
        return {
            'id':response[0]['id'],
            'name':response[0]['name'],
            'creator':response[0]['creator'],
            'details':response[0]['details'],
            'questions':response[0]['questions'],
            'results':response[0]['results'],
            'type':response[0]['type'],
            'introduction':response[0]['introduction'],
            'path':response[0]['path']
        },200
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
