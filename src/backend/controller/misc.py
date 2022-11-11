from fastapi import Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .base import app

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(f'index.html', {'request': request})

@app.get('/favicon.ico', response_class=FileResponse)
async def favicon(request: Request):
    return FileResponse('static/favicon.ico')

@app.get('/{page}', response_class=HTMLResponse)
async def get_page(request: Request, page: str):
    return templates.TemplateResponse(f'{page}.html', {'request': request})