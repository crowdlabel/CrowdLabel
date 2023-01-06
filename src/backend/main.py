import argparse
import uvicorn
import services.database
from controllers.app import app

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bind", default='0.0.0.0:8000')
    parser.add_argument('--docs', action='store_true')
    parser.add_argument('--init-db', action='store_true')
    parser.add_argument('--reset-db', action='store_true')
    args = parser.parse_args()
    return parser, vars(args)

def main():
    parser, args = parse_args()


    if args['reset_db']:
        services.database.reset_db()
    elif args['init_db']:
        services.database.init_db()

    if args['docs']:
        import controllers.app
        controllers.app.generate_docs()
    else:
        uvicorn.run('controllers.app:app', host='0.0.0.0', port=8000, reload=False)

if __name__ == '__main__':
    main()