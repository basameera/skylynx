"""
skylynx utils
===
"""

import json
import yaml
# import numpy as np

__all__ = ["json_write", "json_read",
           "yaml_write", "yaml_read",
           ]


def yaml_write(filename, data):
    """Write .yaml files

    Arguments:
        filename {yaml} -- [path/to/file/name.yaml]
        data {dict} -- [python dictionary object]
    """
    with open(filename, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


def yaml_read(filename):
    """Read .yaml files

    Arguments:
        filename {yaml} -- [path/to/file/name.yaml]

    Returns:
        [dict] -- [python dictionary object]
    """
    with open(filename) as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def json_write(filename, data):
    """Write .json files (with indent and utf-8 encoding)

    Arguments:
        filename {json} -- [path/to/file/name.json]
        data {dict} -- [python dictionary object]
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)


def json_read(filename):
    """Read .json files

    Arguments:
        filename {json} -- [path/to/file/name.json]

    Returns:
        [dict] -- [python dictionary object]
    """
    with open(filename) as f_in:
        return(json.load(f_in))


if __name__ == '__main__':
    pass
