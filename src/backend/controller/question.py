from .base import app
import services.question
from fastapi import APIRouter
from .schemas import *

question_router = APIRouter(prefix='/question')

@app.get('/questions')
async def questions():
    return 'api: questions'

@app.post('/create_question')
async def create_question(details:QuestionInfo):
    response = await services.question.create_question(
        details.type,
        details.prompt,
        details.resource,
        details.options,
        details.task_id
        )
    if response != 'ok':
        return {
            'error': f'{response} already exists'
        }, 400
    else:
        return {
        "type":details.type,
        "prompt":details.prompt,
        "resource":details.resource,
        "options":details.options,
        "task_id":details.task_id
        }, 200
@app.post('/delete_question')
async def delete_question(details:ID):
    response = await services.question.delete_question(details.id)
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
@app.post('/get_question')
async def get_question(details:ID):
    response = await services.question.get_question(details.id)
    if response[0]["status"] != "ok":
        return {
            'error' : f'not found id {details.id}'
        },400
    else :
        return {
            
            "type":response[0]["type"],
            "prompt":response[0]["prompt"],
            "resource":response[0]["resource"],
            "options":response[0]["options"],
            "task_id":response[0]["task_id"]
        
        },200

