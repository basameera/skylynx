"""
Skylynx utils
===
"""

import json
import yaml
from blessings import Terminal
import os
import argparse
import string

__all__ = ["json_write", "json_read", "yaml_write", "yaml_read",
           "pprint", "makedirs", "cli_args",
           ]


def _arg_reform(params):
    alphabet = list(string.ascii_lowercase)
    alphabet.remove('h')
    if len(params) > 25:
        raise ValueError('Cannot handle more than 25 args.')

    if isinstance(params, dict):
        arg_dict = dict()
        for i, (key, value) in enumerate(params.items()):
            arg_dict[alphabet[i]] = (
                key + ' (default: {})'.format(value), value)
        return arg_dict
    else:
        raise TypeError('params should be dict type')


def cli_args(cli_params):
    """[summary]

    Arguments:
        cli_params {dict} -- [A python dict containing, cli argument name and defalut value as key, value pairs]

    Raises:
        TypeError: [Input type can only be dict]

    Returns:
        [dict] -- [A python dict similar to the input, except the values are replaced by user argument values]

    Usage:

        cli_params = dict(task=0,
                      length=10
                      )

        args = cli_args(cli_params)
        task = args['task']
    """

    params = _arg_reform(cli_params)
    # check if params is dict
    if isinstance(params, dict):
        parser = argparse.ArgumentParser(
            description='*** Simple cli args - by Skylynx ***')
        for key, value in params.items():
            parser.add_argument('-'+key, help=value[0], default=value[1])
        output = dict()

        for key1, key2 in dict(zip(cli_params, sorted(parser.parse_args().__dict__))).items():
            output[key1] = parser.parse_args().__dict__[key2]
        return output
    else:
        raise TypeError('params should be dict')


def makedirs(path):
    """Make directories if they don't already exists/

    Arguments:
        path {str} -- ['path/to/the/folder/']
    """
    if not os.path.exists(path):
        os.makedirs(path)


def pprint(input, header=''):
    """Skylynx Pretty Print - Print a python dict object in a human readable form.

    Arguments:
        input {dict} -- [python dictionary]

    Keyword Arguments:
        header {str} -- [Header for pretty print] (default: {''})
    """
    _prettyPrint(input, heading=header)


def _prettyPrint(input, heading='', prev_indent=0):
    terminal = Terminal()
    max_terminal_width = terminal.width
    if isinstance(input, dict):
        zzz = []
        _getMaxLen(input, zzz)
        maxFooterLen = min([max(zzz), max_terminal_width])
        if max(zzz) > max_terminal_width:
            maxFooterLen -= 2

        maxKeyLen = 0
        maxValLen = 0
        for key, value in input.items():
            if len(str(key)) > maxKeyLen:
                maxKeyLen = len(str(key))
            if len(str(value)) > maxValLen:
                maxValLen = len(str(value))

        a = maxFooterLen - len(str(heading))
        if heading == '':
            a += 2
        # header
        if prev_indent == 0:
            _printLine(int(a/2), end='')
            if heading != '':
                print('', heading, '', end='')
            _printLine(a - int(a/2))

        # data
        for key, value in input.items():
            for _ in range(prev_indent):
                print(' ', end='')
            print(str(key), end='')
            klen = len(str(key))
            for _ in range(maxKeyLen - klen):
                print(' ', end='')

            print(':', end='')

            if isinstance(value, dict):
                print('')
                _prettyPrint(value, prev_indent=prev_indent + maxKeyLen + 1)
            else:
                print('', value)

        # footer
        if prev_indent == 0:
            _printLine(maxFooterLen + 2, symbol='-')

    else:
        raise TypeError('Input should be a Dictionary object.')


def _printLine(len, symbol='=', end='\n'):
    if isinstance(len, int):
        for _ in range(len):
            print(symbol, end='')
        print(end, end='')
    else:
        raise TypeError('Input should be an int value.')


def _getMaxLen(input, output, prev_indent=0):
    if isinstance(input, dict):
        maxKeyLen = 0
        maxValLen = 0
        for key, value in input.items():
            if len(str(key)) > maxKeyLen:
                maxKeyLen = len(str(key))
            if len(str(value)) > maxValLen:
                maxValLen = len(str(value))

        rawValLen = 0
        # data
        for key, value in input.items():
            klen = len(str(key))

            if isinstance(value, dict):
                _getMaxLen(value, output,
                           prev_indent=prev_indent + maxKeyLen + 1)
            else:
                if len(str(value)) > rawValLen:
                    rawValLen = len(str(value))

        a = maxKeyLen + prev_indent + rawValLen
        output.append(a)

    else:
        raise TypeError('Input should be a Dictionary object.')


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
