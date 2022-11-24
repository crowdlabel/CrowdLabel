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
            'name': details.name,
            'creator': details.creator,
            'details': details.details,
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
            'details':response[0]['details']
        },200

async def download_results():
    return await download_file('main.py')
