import json
from collections import ChainMap


def load_settings(env):
    with open('{}.json'.format(env)) as f:
        settings = json.load(f)
    return settings


def chain_recursively(d1, d2):
    chain = ChainMap(d1, d2)
    for k, v in d1.items():
        if isinstance(v, dict) and k in d2:
            chain[k] = chain_recursively(d1[k], d2[k])
    return chain
