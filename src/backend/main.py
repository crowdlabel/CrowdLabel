import uvicorn
from controller.controllers import *
from fastapi.openapi.utils import get_openapi
import json
import argparse

def generate_doc():
    with open('openapi.json', 'w') as f:
        json.dump(get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ), f)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--docs', action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    
    args = parse_args()
    if args.docs:
        generate_doc()
    else:
        uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=False)
    # to view API documentation, visit 127.0.0.1:8000/docs
