import argparse
import json
import uvicorn
from fastapi.openapi.utils import get_openapi
from controllers.routers import app
from services.database import init_models_sync

def generate_docs():
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
    parser.add_argument('--init_db', action='store_true')
    args = parser.parse_args()
    return args


def run():
    # to view API documentation, visit 127.0.0.1:8000/docs
    args = parse_args()

    if args.init_db:
        init_models_sync()
    if args.docs:
        generate_docs()
        return

    uvicorn.run('main:app', host='localhost', port=8000, reload=False)
    



if __name__ == '__main__':
    run()


