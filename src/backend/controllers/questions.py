import fastapi
from fastapi import status, APIRouter
from fastapi.responses import StreamingResponse, FileResponse
from .base import app
import services.questions
import services.tasks
import schemas.tasks
import schemas.questions
from .jsondocumentedresponse import JSONDocumentedResponse, create_documentation, not_found_jdr, forbidden_jdr
import controllers.tasks
import services.questions

from services.questions import question_service
from services.tasks import task_service

import schemas.answers
from utils.filetransfer import download_file

from .auth import Depends, get_current_user

router = APIRouter(prefix='/tasks/{task_id}/questions')


###############################################################################
question_not_found_error = JSONDocumentedResponse(
    status.HTTP_404_NOT_FOUND,
    'Question not found'
)
@router.get('/{question_id}',
    **create_documentation([question_not_found_error])
)
async def get_question(question_id: int, task=Depends(controllers.tasks.get_task), current_user=Depends(get_current_user)):
    question = await question_service.get_question(task, question_id)
    if not question:
        return question_not_found_error.response()
    
    return question
###############################################################################
create_answer_success = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Answer created successfully. Answer is returned',
    schemas.answers.Answer,
)
create_answer_failed = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Answer not created. Error message is returned',
    schemas.tasks.ErrorResponse,
)
@router.put('/{question_id}/answer',
    **create_documentation([create_answer_success, create_answer_failed])
)
async def create_answer(
    answer: schemas.answers.AnswerRequest,
    task_id: int=fastapi.Path(), question_id: int=fastapi.Path(),
    current_user=Depends(get_current_user(['respondent']))
):
    task = await task_service.get_task(task_id)
    if not task:
        return not_found_jdr.response()
    if current_user.username not in task.respondents_claimed:
        return forbidden_jdr.response()
    question = question_service.get_question(task, question_id)
    if not question:
        return not_found_jdr.response()

    response = await question_service.create_answer(current_user, task, question, answer)

    if response:
        return create_answer_failed.response(schemas.tasks.ErrorResponse(response))    
    return create_answer_success.response(answer)
###############################################################################
get_answer_resource_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Resource retrieved successfully',
)
get_answer_resource_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'No resource associated with this quesiton',
)
@router.get('/{question_id}/resource',
    description='Get the resource (if any) associated with the question',
    **create_documentation([get_answer_resource_success_jdr, forbidden_jdr, not_found_jdr])
)
async def get_question_resource(
    task_id: int=fastapi.Path(), question_id: int=fastapi.Path(),
    current_user=Depends(get_current_user()),
):
    task = await task_service.get_task(task_id)
    if not task:
        return not_found_jdr.response()
    if (current_user.username not in task.respondents_claimed or
        current_user.username != task.requester):
        # only allow the requester who created the task or the respondents who claimed this task see the resource
        return forbidden_jdr.response()
    question = question_service.get_question(task, question_id)
    if not question:
        return not_found_jdr.response()
    if not question.resource:
        return get_answer_resource_failed_jdr.response()

    resource_path = task.resource_path / question.resource

    return download_file(resource_path)

    # TODO: return the file