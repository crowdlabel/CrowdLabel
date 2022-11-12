from .base import app
from .login_required import login_required
from utils.filetransfer import *

@app.get('/tasks')
@login_required
async def tasks():
    return 'api: tasks'

@app.get('/task/<id>')
@login_required
def task(id):
    return 'requested task with id ' + str(id)

@app.post(
    '/upload_task',
)
async def upload_task(in_file: UploadFile, data: str):
    upload_file(in_file, 'upload.test')


@app.get(
    '/download_results',
)
async def download_results():
    return await download_file('main.py')
