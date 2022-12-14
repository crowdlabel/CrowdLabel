import argparse
import json
from datetime import datetime
import uvicorn
from fastapi.openapi.utils import get_openapi
from controllers.routers import app
import schemas.tasks

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
    args = parser.parse_args()
    return args


def main():
    # to view API documentation, visit 127.0.0.1:8000/docs
    args = parse_args()
    if args.docs:
        generate_docs()
        return

    uvicorn.run('main:app', host='localhost', port=8000, reload=False)
    

if __name__ == '__main__':
    main()
    """ task1 = schemas.tasks.Task(
        task_id = 1,
        creator = 'test',
        credits = 10,
        date_created=datetime.utcnow(),
        name = 'test name',
        responses_required = 1,
        questions=[]
    )
    print(task1)
    from time import sleep
    sleep(1)
    task2 = schemas.tasks.Task(
        task_id = 2,
        creator = 'test',
        credits = 10,
        date_created=datetime.utcnow(),

        name = 'test name',
        responses_required = 1,
        questions=[]
    )
    print(task2)
    task1.set_id(3)
    task2.set_id(4)
    print(task1)
    print(task2) """

