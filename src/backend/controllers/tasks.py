from fastapi import Depends, UploadFile, status
from fastapi.routing import APIRouter
from utils.filetransfer import download_file, upload_file
from .auth import get_current_user
import services.tasks
import services.users
from datetime import datetime
from .jsondocumentedresponse import JSONDocumentedResponse, create_documentation
import schemas.tasks

router = APIRouter()


get_task_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Successfully queried tasks.',
    schemas.tasks.TasksResponse
)
get_task_failed_hdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task query failed.',
    schemas.tasks.ErrorResponse
)
@router.get('/',
    **create_documentation([get_task_success_jdr, get_task_failed_hdr])
)
async def get_tasks(query: schemas.tasks.TasksRequest, current_user=Depends(get_current_user(['admin', 'respondent']))):
    """
    Task search
    """
    tasks = await services.tasks.get_tasks(current_user, **query)
    if isinstance(tasks, str):
        return get_task_failed_hdr.response(tasks)
    return get_task_success_jdr.response(tasks)

@router.post('/upload')
async def upload_task(in_file: UploadFile, current_user=Depends(get_current_user(['requester']))):
    filename = 'upload_' + current_user.username + '_' + datetime.utcnow().strftime('%Y-%m-%d_%H.%M.%S.%f')[:-3] + '.zip'
    upload_file(in_file, filename)
    result = await services.tasks.process_task_archive(filename)


""" @app.post('/create_task')
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
        }, 200 """

@router.delete('/{task_id}')
async def delete_task(task_id: int, current_user=Depends(get_current_user(['requester']))):
    task = await services.tasks.get_task(task_id)
    if not task:
        return 400
    if current_user.username != task.creator:
        return 400

    response = await services.tasks.delete_task(task_id)
    return {'task_id': task_id}, status.HTTP_200_OK if response else status.HTTP_400_BAD_REQUEST

""" @router.patch('/{task_id}')
async def edit_task(details: TaskDetails):
    response = await ts.edit_task(
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
        } """

@router.get('/{task_id}')
async def get_task(task_id: int, current_user=Depends(get_current_user())):

    task = await ts.get_task(task_id)
    if not task:
        return {'description': 'Task not found'}, status.HTTP_404_NOT_FOUND
    if task.creator == current_user:
        # allow the owner to see the full details of the task
        return task

    # do not show the answers to anyone else
    for i in range(len(task.questions)):
        task.questions[i].answers = None

    return task

    """ 
    
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

    """


claim_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task claimed successfully.',
    schemas.tasks.Task,
)
claim_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task claim failed.',
    schemas.tasks.ErrorResponse,
)
@router.post('/{task_id}/claim',
    **create_documentation([claim_success_jdr, claim_failed_jdr])
)
async def claim_task(task_id: int, current_user=Depends(get_current_user(['respondent']))):
    task = await services.tasks.get_task(task_id)
    if len(task.respondents_claimed) + len(task.respondents_completed) >= task.responses_required:
        return claim_failed_jdr(schemas.tasks.ErrorResponse('No claims left'))
    
    if task_id in current_user.tasks_claimed or task_id in current_user.tasks_completed:
        return claim_failed_jdr(schemas.tasks.ErrorResponse('Already claimed'))

    current_user.tasks_claimed.append(task_id)

    task.answers = None

    return claim_success_jdr.response(task)

@router.get('/{task_id}/download',)
async def download_task_results(task_id: int, current_user=Depends(get_current_user(['requester']))):
    filename = await services.tasks.create_task_results_file(task_id)
    return await download_file(filename)

@router.patch('/{task_id}')
async def edit_task(task_id: int, current_user=Depends(get_current_user)):
    return 'editing task ' + str(task_id)