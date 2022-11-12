import uvicorn
from controller.controllers import *

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=False)
    # to view API documentation, visit 127.0.0.1:8000/docs
