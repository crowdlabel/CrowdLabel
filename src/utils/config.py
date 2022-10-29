import yaml
from pathlib import Path
from pprint import pprint

base_dir = Path(__file__).parents[1]
config_filename = 'config.yaml'

with open(base_dir / config_filename, encoding='utf8') as f:
    config = yaml.load(f.read(), yaml.FullLoader)

def get_config(key, default=None):
    data = config
    for subkey in key.split('.'):
        data = data.get(subkey, default)
    return data

if __name__ == '__main__':
    pprint(config)
