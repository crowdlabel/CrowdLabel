import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--config', default='config.yaml')
group = parser.add_mutually_exclusive_group()
group.add_argument('--docs', action='store_true')
group.add_argument('--init_db', action='store_true')
group.add_argument('--prod', action='store_true')
args = parser.parse_args()

import utils.config
utils.config.load_config(args.config)

if args.init_db:
    from services.database import init_models_sync
    init_models_sync()
elif args.docs:
    import controllers.routers
    controllers.routers.generate_docs()
else:
    root_path = ''
    if args.prod:
        root_path = '/api'
    import uvicorn
    uvicorn.run('controllers.routers:app', host='0.0.0.0', port=8000, reload=False, root_path=root_path)