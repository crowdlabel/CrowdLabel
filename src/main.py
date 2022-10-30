import platform
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


@app.get('/')
def index():
    return HTMLResponse('test')


from utils import config

print(config.get_config('db.password'))