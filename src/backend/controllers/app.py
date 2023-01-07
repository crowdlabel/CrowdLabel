import json
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRouter
from starlette.middleware.cors import CORSMiddleware


origins = [
    'http://localhost:8082',
    'https://crowdlabel.org',
]

app = FastAPI(
    title='CrowdLabelAPI',
    description='API for CrowdLabel',
    version='0.1.0',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get(app.root_path + '/openapi.json')
def custom_swagger_ui_html():
    return app.openapi()


app_router = APIRouter(prefix='')
from . import auth, tasks, users, questions
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