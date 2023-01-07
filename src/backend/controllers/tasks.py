import pathlib
from fastapi import Depends, UploadFile, status
from fastapi.routing import APIRouter
from .auth import get_current_user
from .documentedresponse import JSONDocumentedResponse, MediaDocumentedResponse, create_documentation, forbidden_jdr, not_found_jdr
import schemas.tasks
import schemas.questions
import schemas.users
import services.tasks
import services.users
import utils.config
from utils.datetime_str import datetime_now_str
from utils.filetransfer import download_file, upload_file

TASK_UPLOAD_DIR = pathlib.Path(utils.config.config['directories']['tasks'])
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
async def search_tasks(query: schemas.tasks.TaskSearchRequest, current_user=Depends(get_current_user())):
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
    **create_documentation([upload_success_jdr, upload_failed_jdr, forbidden_jdr])
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
    from pprint import pprint
    await task_service.remove_answers(current_user, task)

    return get_task_success_jdr.response(task, exclude={'resource_path'})




###############################################################################
task_delete_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task deleted successfully',
)
task_delete_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task not deleted',
    schemas.tasks.ErrorResponse
)
@router.delete('/{task_id}',
    **create_documentation([task_delete_success_jdr, task_delete_failed_jdr, forbidden_jdr, not_found_jdr])
)
async def delete_task(task_id: int, current_user: schemas.users.Requester=Depends(get_current_user(['requester']))):
    task = await task_service.get_task(task_id)
    if not task:
        return not_found_jdr.response()
    if current_user.username != task.requester:
        return forbidden_jdr.response()
    response = await task_service.delete_task(task_id)
    if response:
        return forbidden_jdr.response(schemas.tasks.ErrorResponse(response))
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
download_task_success_jdr = MediaDocumentedResponse(
    status.HTTP_200_OK,
    'Task downloaded successfully',
    'application/zip'
)
download_task_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task not downloaded',
    schemas.tasks.ErrorResponse,
)
@router.get('/{task_id}/download',
    description='Download results',
    **create_documentation([download_task_success_jdr, download_task_failed_jdr, forbidden_jdr, not_found_jdr]),
)
async def download_task_results(task_id: int, current_user=Depends(get_current_user(['requester']))):
    task = await task_service.get_task(task_id)
    if not task:
        return not_found_jdr.response()
    if current_user.username != task.requester:
        return forbidden_jdr.response()
    response = await task_service.create_task_results_file(task_id)
    if not isinstance(response, pathlib.Path):
        return download_task_failed_jdr.response(schemas.tasks.ErrorResponse(error=response))
    return await download_file(response, media_type='application/json')
###############################################################################

""" @router.patch('/{task_id}')
async def edit_task(task_id: int, current_user=Depends(get_current_user)):
    return 'editing task ' + str(task_id) """
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
async def get_cover(task_id: int, current_user: schemas.users.User=Depends(get_current_user())):
    task = await task_service.get_task(task_id)
    if not task:
        return not_found_jdr.response()
    
    if not task.cover_image:
        return get_cover_failed_jdr.response()

    resource_path = task.resource_path / task.cover_image

    return await download_file(resource_path, media_type='image/jpeg')
###############################################################################

progress_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Index of the last completed question',
    schemas.tasks.TaskProgress,
)
@router.get('/{task_id}/progress',
    description='Respondent\'s progress within a task, which is the highest index answered question. -1 if no questions have been answered yet.',
    **create_documentation([not_found_jdr, forbidden_jdr])
)
async def get_progress(task_id, current_user: schemas.users.User=Depends(get_current_user(['respondent']))):
    task = await task_service.get_task(task_id)
    if not isinstance(task, schemas.tasks.Task):
        return not_found_jdr.response()

    if current_user.username not in task.respondents_claimed:
        return forbidden_jdr.response()

    progress_index = -1

    for i in range(len(task.questions) - 1, -1, -1):
        for answer in task.questions[i].answers:
            if answer.respondent == current_user.username:
                progress_index = i
                break
        if progress_index != -1:
            break

    return progress_jdr.response(schemas.tasks.TaskProgress(progress=progress_index))
###############################################################################
complete_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task completed successfully'
)
complete_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task not completed successfully as there remains unanswered questions',
    schemas.tasks.ErrorResponse
)
@router.post('/{task_id}/complete',
    description='For the respondent to mark the task as completed',
    **create_documentation([complete_success_jdr, complete_failed_jdr, not_found_jdr, forbidden_jdr])
)
async def complete(task_id: int, current_user: schemas.users.User=Depends(get_current_user(['respondent']))):
    task = await task_service.get_task(task_id)
    if not isinstance(task, schemas.tasks.Task):
        return not_found_jdr.response()
    if current_user.username not in task.respondents_claimed:
        return forbidden_jdr.response()
    
    response = await task_service.complete(task_id, current_user.username)
    if response:
        return complete_failed_jdr.response(schemas.tasks.ErrorResponse(error=response))

    return complete_success_jdr

