import json
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRouter
from .base import app

from . import auth, tasks, users, questions

app_router = APIRouter(prefix='')

app_router.include_router(auth.router, prefix='', tags=['auth'])
app_router.include_router(users.router, prefix='/users', tags=['users'])
app_router.include_router(tasks.router, prefix='/tasks', tags=['tasks'])
app_router.include_router(questions.router, prefix='', tags=['questions'])



app.include_router(app_router)


def generate_docs():
    with open('openapi.json', 'w') as f:
        json.dump(get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ), f)