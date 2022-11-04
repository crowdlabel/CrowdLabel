from .base import app
from .login_required import login_required

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
def upload_task():
    pass