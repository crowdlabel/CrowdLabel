from fastapi import Depends, UploadFile, status
from fastapi.responses import FileResponse
from fastapi.routing import APIRouter
from utils.filetransfer import download_file, upload_file
from .auth import get_current_user
import services.tasks
import services.users
from .documentedresponse import JSONDocumentedResponse, MediaDocumentedResponse, create_documentation, forbidden_jdr, not_found_jdr
import schemas.tasks
import schemas.questions
import schemas.users
from utils.datetime_str import datetime_now_str
from typing import Optional
from utils.config import get_config
import pathlib

TASK_UPLOAD_DIR = pathlib.Path(get_config('file_locations.tasks'))
router = APIRouter()
task_service = services.tasks.Tasks()


###############################################################################
search_tasks_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Successfully queried tasks.',
    schemas.tasks.TaskSearchResponse
)
search_tasks_failed_hdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task query failed.',
    schemas.tasks.ErrorResponse
)
@router.put('/',
    description=task_service.search.__doc__ + schemas.tasks.TaskSearchRequest.__doc__,
    **create_documentation([search_tasks_success_jdr, search_tasks_failed_hdr])
)
async def search_tasks(query: schemas.tasks.TaskSearchRequest, current_user=Depends(get_current_user(['respondent']))):
    """
    Task search
    """
    # TODO: complete arguments
    tasks = await task_service.search(current_user, query)
    if isinstance(tasks, str):
        return search_tasks_failed_hdr.response(schemas.tasks.ErrorResponse(tasks))

    # exclude tasks.questions and resource path
    for i in range(len(tasks[0])):
        tasks[0][i].resource_path = None
        tasks[0][i].questions = len(tasks[0][i].questions)

    return search_tasks_success_jdr.response(schemas.tasks.TaskSearchResponse(tasks=tasks[0], total=tasks[1]), exclude={'questions'})
###############################################################################
upload_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task uploaded and created successfully',
    list[schemas.questions.Question]
)
upload_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task not created',
    schemas.tasks.ErrorResponse
)
@router.post('/upload',
    **create_documentation([upload_success_jdr, upload_failed_jdr])
)
async def upload_task(task_file: UploadFile, current_user=Depends(get_current_user(['requester']))):
    out_path = TASK_UPLOAD_DIR / ('upload_' + current_user.username + '_' + datetime_now_str() + '.zip')
    await upload_file(task_file, out_path)
    task = await task_service.process_task_archive(out_path)
    if isinstance(task, str):
        return upload_failed_jdr.response(schemas.tasks.ErrorResponse(error=task))
    task = await task_service.create_task(current_user, task, out_path.parent / out_path.stem)
    if isinstance(task, str):
        return upload_failed_jdr.response(schemas.tasks.ErrorResponse(error=task))
    return upload_success_jdr.response(task, exclude={'resource_path'})
###############################################################################




""" create_task_success_jdr = JSONDocumentedResponse(
    status.HTTP_201_CREATED,
    'Task created successfully',
    schemas.tasks.Task
)
create_task_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task not created',
    schemas.tasks.ErrorResponse
)
@router.post('/create',
    **create_documentation([create_task_success_jdr, create_task_failed_jdr])
)
async def create_task(task: schemas.tasks.CreateTaskRequest, questions_file: UploadFile,

    current_user=Depends(get_current_user(['requester']))
):

    cover_filename = 'cover_' + current_user.username + datetime_now_str() + '.png'
    questions_filename = 'questions_' + current_user.username + datetime_now_str() + '.zip'

    await upload_file(questions_file, questions_filename)

    #questions = await task_service.process_task_archive(questions_filename)

    result = await task_service.create_task(
        creator=current_user,
        name=task.name,
        description=task.description,
        introduction=task.introduction,
        cover_filename=cover_filename if cover else None,
        responses_required=task.responses_required,
        credits=task.credits,
    )

    if not isinstance(result, schemas.tasks.Task):
        return create_task_failed_jdr(schemas.tasks.ErrorResponse(result))

    if cover:
        await upload_file(cover, 'cover_' + current_user.username + datetime_now_str() + '.png') """


###############################################################################
get_task_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task retrieved successfully.',
    schemas.tasks.Task,
)
@router.get('/{task_id}',
    description='Get a task based on its task_id',
    **create_documentation([get_task_success_jdr, not_found_jdr, forbidden_jdr])    
)
async def get_task(task_id: int, current_user: schemas.users.User=Depends(get_current_user())):
    task = await task_service.get_task(task_id=task_id)
    if not task:
        return not_found_jdr.response()
    if (current_user.username != task.requester and
        current_user.username not in task.respondents_claimed):

        return forbidden_jdr.response()
    return get_task_success_jdr.response(task, exclude={'resource_path'})

###############################################################################
task_delete_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task deleted successfully',
)
@router.delete('/{task_id}',
    **create_documentation([task_delete_success_jdr, forbidden_jdr, not_found_jdr])
)
async def delete_task(task_id: int, current_user=Depends(get_current_user(['requester']))):
    task = await task_service.get_task(task_id)
    if not task:
        return not_found_jdr.response()
    response = await task_service.delete_task(task_id)
    if response == 'forbidden':
        return forbidden_jdr.response()
    return task_delete_success_jdr.response()
###############################################################################
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
    task = await task_service.claim_task(current_user.username,task_id)
    if not isinstance(task, schemas.tasks.Task):
        return claim_failed_jdr.response(schemas.tasks.ErrorResponse(error=task))
    return claim_success_jdr.response(task)
###############################################################################

@router.get('/{task_id}/download',)
async def download_task_results(task_id: int, current_user=Depends(get_current_user(['requester']))):
    filename = await task_service.create_task_results_file(task_id)
    return await download_file(filename)
###############################################################################

@router.patch('/{task_id}')
async def edit_task(task_id: int, current_user=Depends(get_current_user)):
    return 'editing task ' + str(task_id)
###############################################################################
get_cover_success_jdr = MediaDocumentedResponse(
    status.HTTP_200_OK,
    'Cover image retrieved successfully',
    'image/*'
)
get_cover_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Cover image retrieval failed - no cover image was specified'
)
@router.get('/{task_id}/cover-image',
    description='Get cover image',
    **create_documentation([get_cover_success_jdr, get_cover_failed_jdr, forbidden_jdr, not_found_jdr]),
)
async def get_cover(task_id: int, current_user: schemas.users.User=Depends(get_current_user([]))):
    task = await task_service.get_task(task_id)
    if not task:
        return not_found_jdr.response()

    if (current_user.username not in task.respondents_claimed and
        current_user.username != task.requester):
        # only allow the requester who created the task or the respondents who claimed this task see the resource
        return forbidden_jdr.response()
    
    if not task.cover_image:
        return get_cover_failed_jdr.response()

    resource_path = task.resource_path / task.cover_image

    return await download_file(resource_path)