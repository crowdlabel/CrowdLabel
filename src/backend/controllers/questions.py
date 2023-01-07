import fastapi
from fastapi import status, APIRouter
import services.tasks
import schemas.tasks
import schemas.questions
from .documentedresponse import JSONDocumentedResponse, create_documentation, not_found_jdr, forbidden_jdr
import services.questions
from services.questions import question_service
from services.tasks import task_service

import schemas.answers
from utils.filetransfer import download_file

from .auth import Depends, get_current_user

router = APIRouter(prefix='/tasks/{task_id}/questions')


get_question_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Question retrieved successfully',
    schemas.questions.Question
)
@router.get('/{question_id}',
    **create_documentation([get_question_success_jdr, not_found_jdr, forbidden_jdr])
)
async def get_question(task_id: int=fastapi.Path(), question_id: int=fastapi.Path(), current_user=Depends(get_current_user())):
    task = await task_service.get_task(task_id)
    if not isinstance(task, schemas.tasks.Task):
        return not_found_jdr.response()
    await task_service.remove_answers(current_user, task)

    for question in task.questions:
        if question.question_id == question_id:
            return get_question_success_jdr.response(question)

    return not_found_jdr.response()
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
    answer: schemas.answers.AnswerTypes,
    task_id: int=fastapi.Path(), question_id: int=fastapi.Path(),
    current_user=Depends(get_current_user(['respondent']))
):
    task = await task_service.get_task(task_id)
    if not task:
        return not_found_jdr.response()
    if current_user.username not in task.respondents_claimed:
        return forbidden_jdr.response()
    question = await question_service.get_question(task, question_id)
    if not question:
        return not_found_jdr.response()

    response = await question_service.create_answer(task_id, question_id, current_user, answer)

    if response:
        return create_answer_failed.response(schemas.tasks.ErrorResponse(error=response))    
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

    if (current_user.username not in task.respondents_claimed and
        current_user.username != task.requester):
        # only allow the requester who created the task or the respondents who claimed this task see the resource
        return forbidden_jdr.response()
    question = await question_service.get_question(task, question_id)
    if not question:
        return not_found_jdr.response()
    if not question.resource:
        return get_answer_resource_failed_jdr.response()

    resource_path = task.resource_path / question.resource

    return await download_file(resource_path)