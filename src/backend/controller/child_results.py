from .base import app
from utils.filetransfer import *
import services.child_results
from fastapi import APIRouter
from .schemas import *

result_router = APIRouter(prefix='/child_result')

@app.get('/child_results')
async def child_results():
    return 'api: child_results'

@app.post('/create_child_result')
async def create_result(details:ChildResultInfo):
    response = await services.child_results.create_result(
        details.response,
        details.result_id)
    if response[0]['status'] != 'ok':
        return {
            'error': f'{response} already exists'
        }, 400

    
    else:
        return {
            'result_id': details.result_id,
            'response':details.response
        }, 200
@app.post('/delete_child_result')
async def delete_result(details:ID):
    response = await services.child_results.delete_result(details.id)
    if response[0]['status'] != 'ok':
        return {
            'error' : f'delete failed'
        },400
    else :
        return {
            'id':details.id
        },200
@app.post('/edit_child_result')
async def edit_result(details:ChildTaskResponse):
    response = await services.child_results.edit_result(
        details.id,
        details.response
    )
    if response[0]['status'] != 'ok':
        return {
            'error': 'edit failed'
        },400
    else:
        return {
            'id':response[0]['id'],
            'result_id':response[0]['result_id'],
            'response':response[0]['response']
        }
@app.post('/get_child_result')
async def get_result(details:ID):
    response = await services.child_results.get_result(details.id)
    if response[0]["status"] != "ok":
        return {
            'error' : f'not found id {details.id}'
        },400
    else :
        return {
            'id':response[0]['id'],
            'result_id':response[0]['result_id'],
            'response':response[0]['response']
        },200
@result_router.get('/')
def result(id):
    return 'requested result with id ' + str(id)
