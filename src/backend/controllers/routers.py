from fastapi.routing import APIRouter
from .base import app

from . import auth, tasks, users

app_router = APIRouter(prefix='')

app_router.include_router(auth.router, prefix='', tags=['auth'])
app_router.include_router(tasks.router, prefix='/tasks', tags=['tasks'])
app_router.include_router(users.router, prefix='/users', tags=['users'])

app.include_router(app_router)