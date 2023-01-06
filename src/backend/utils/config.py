import yaml
import pathlib
from frozendict import frozendict


with open(pathlib.Path(__file__).parents[1] / 'config.yaml', encoding='utf8') as f:
    config = frozendict(**yaml.load(f.read(), yaml.FullLoader))

pathlib.Path(config['database_filename']).parent.mkdir(parents=True, exist_ok=True)

for dir in config['directories']:
    path = pathlib.Path(config['directories'][dir])
    if not path.suffix:
        path.mkdir(parents=True, exist_ok=True)