import uvicorn
from controller.controllers import *


from utils.hasher import hash



if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8081, reload=False)
    # to view API documentation, visit 127.0.0.1:8000/docs
