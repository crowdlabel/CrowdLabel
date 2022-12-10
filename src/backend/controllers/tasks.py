from fastapi import Depends, UploadFile, status
from fastapi.routing import APIRouter
from utils.filetransfer import download_file, upload_file
from .auth import get_current_user
import services.tasks as ts
import services.users as us

router = APIRouter()

@router.get('/')
async def get_tasks(current_user=Depends(get_current_user)):
    """
    Task search
    """
    tasks = await ts.get_tasks()
    print(tasks)
    return tasks

@router.post('/upload')
async def upload_task(in_file: UploadFile, current_user=Depends(get_current_user)):
    upload_file(in_file, 'upload.test')
    


@router.post('/create')
async def create_task(details: str, current_user=Depends(get_current_user)):
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

@router.delete('/{task_id}')
async def delete_task(task_id: int, current_user=Depends(get_current_user)):
    task = ts.get_task(task_id)
    if not task:
        return 400

    if current_user != task.creator:
        return 400

    response = await ts.delete_task(task_id)
    return {'task_id': task_id}, status.HTTP_200_OK if response else status.HTTP_400_BAD_REQUEST

""" @router.patch('/{task_id}')
async def edit_task(details: TaskDetails):
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
            
        } """

@router.get('/{task_id}')
async def get_task(task_id: int, current_user=Depends(get_current_user(['respondent']))):

    task = await ts.get_task(task_id)
    if not task:
        return {'description': 'Task not found'}, status.HTTP_404_NOT_FOUND
    if task.creator == current_user:
        # allow the owner to see the full details
        return task

    # do not show the answers to anyone else
    for i in range(len(task.questions)):
        task.questions[i].answers = None

    return task

    """ return {
        'id':response[0]['id'],
        'name':response[0]['name'],
        'creator':response[0]['creator'],
        'details':response[0]['details'],
        'questions':response[0]['questions'],
        'results':response[0]['results']
    }, 200 """



@router.get('/{task_id}/download-results',)
async def download_task_results(task_id: int, current_user=Depends(get_current_user)):
    filename = ts.create_task_results_file(task_id)
    return await download_file(filename)

@router.patch('/{task_id}')
async def edit_task(task_id: int, current_user=Depends(get_current_user)):
    return 'editing task ' + str(task_id)