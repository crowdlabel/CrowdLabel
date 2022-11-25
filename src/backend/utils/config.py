import yaml
from pathlib import Path

data = None

def load_config(filename=Path(__file__).parents[1] / 'config.yaml'):
    global data
    with open(filename, encoding='utf8') as f:
        data = yaml.load(f.read(), yaml.FullLoader)

def get_config(key, default=None):
    if data == None:
        raise Exception('Config not loaded')
    for subkey in key.split('.'):
        data = data.get(subkey, default)
    return data