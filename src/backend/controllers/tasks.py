from fastapi import Depends, UploadFile
from fastapi.routing import APIRouter
from utils.filetransfer import download_file, upload_file
from .auth import User, get_current_user
import services.task as ts
from schemas.schemas import *


router = APIRouter()

@router.get('/')
async def get_tasks(current_user: User = Depends(get_current_user)):
    """
    Task search
    """
    tasks = ts.get_tasks()
    print(tasks)
    return tasks

@router.post('/')
async def create_task(details: TaskInfo):
    response = await ts.create_task(
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

@router.post(
    '/upload',
)
async def upload_task(in_file: UploadFile, data: str):
    upload_file(in_file, 'upload.test')


@router.delete('/')
async def delete_task(details:ID):
    response = await ts.delete_task(details.id)
    if response[0]['status'] != 'ok':
        return {
            'error' : f'delete failed'
        },400
    else :
        return {
            'id':details.id
        },200

@router.patch('/')
async def edit_task(details:TaskDetails):
    response = await ts.edit_task(
        details.id,
        details.details
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
            'details':response[0]['details']
            
        }

    
@router.get('/<id>')
async def get_task(id: ID, current_user = Depends(get_current_user)):
    response = await ts.get_task(id)
    if response[0]["status"] != "ok":
        return {
            'error' : f'not found id {id}'
        },400
    else :
        return {
            'id':response[0]['id'],
            'name':response[0]['name'],
            'creator':response[0]['creator'],
            'details':response[0]['details'],
            'questions':response[0]['questions'],
            'results':response[0]['results']
        },200


@router.get(
    '/<id>/download-results',
)
async def download_task_results(id: ID, current_user = Depends(get_current_user)):
    ts.create_task_results_file(id)
    return await download_file('main.py')