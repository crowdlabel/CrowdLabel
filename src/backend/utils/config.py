import yaml
from pathlib import Path

""" with open('config.yaml', encoding='utf8') as f:
    settings = yaml.load(f.read(), yaml.FullLoader)

def load_config(filename=Path(__file__).parents[1] / 'config.yaml'):
    global data
    with open(filename, encoding='utf8') as f:
        data = yaml.load(f.read(), yaml.FullLoader)

def get_config(key, default=None):
    data = settings
    for subkey in key.split('.'):
        data = data.get(subkey, default)
    return data """

from pprint import pprint
from frozendict import frozendict

def load_config(filename=Path(__file__).parents[1] / 'config.yaml'):
    global config
    with open(filename, encoding='utf8') as f:
        config = frozendict(**yaml.load(f.read(), yaml.FullLoader))
        #print('Config:')
        #pprint(dict(config))