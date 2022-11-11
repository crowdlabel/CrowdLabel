import uvicorn
from controller.user import *
from controller.hello import *

from fastapi import Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=80, reload=False)
    # to view API documentation, visit 127.0.0.1:8000/docs