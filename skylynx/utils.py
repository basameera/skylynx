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
import datetime

__all__ = ["json_write", "json_read", "yaml_write", "yaml_read", "pprint", "makedirs", "cli_args", "clog",

           ]


class tcolors:
    """Terminal Colors
    ---

    https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
    """
    FG_BLACK = '\033[90m'
    FG_RED = '\033[91m'
    FG_GREEN = '\033[92m'
    FG_YELLOW = '\033[93m'
    FG_BLUE = '\033[94m'
    FG_MAGENTA = '\033[95m'
    FG_CYAN = '\033[96m'
    FG_WHITE = '\033[97m'

    BG_BLACK = '\033[100m'
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    BG_MAGENTA = '\033[105m'
    BG_CYAN = '\033[106m'
    BG_WHITE = '\033[107m'


class tformat:
    """Terminal formatting
    ---

    https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
    """
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


class vcolors:
    """Verbose Colors
    ---

    https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
    """
    INFO = tcolors.FG_GREEN
    WARNING = tcolors.FG_YELLOW
    ERROR = tcolors.FG_RED
    CRITICAL = tformat.BOLD + tformat.UNDERLINE + tcolors.FG_RED


def clog(*args, end='\n', verbose='DEBUG'):
    """Logger with date-time and font coloring

    Parameters
    ----------
    end : str, optional
        End character, by default '\\n'
    verbose : str, optional
        DEBUG, INFO, WARNING, ERROR, CRITICAL, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, by default 'DEBUG'
    """
    if verbose == 'DEBUG':
        _print(*args, end=end)
    elif verbose == 'INFO':
        _info(*args, end=end)
    elif verbose == 'WARNING':
        _warn(*args, end=end)
    elif verbose == 'ERROR':
        _error(*args, end=end)
    elif verbose == 'CRITICAL':
        _critical(*args, end=end)

    elif verbose == 'RED':
        _red(*args, end=end)
    elif verbose == 'GREEN':
        _green(*args, end=end)
    elif verbose == 'YELLOW':
        _yellow(*args, end=end)
    elif verbose == 'BLUE':
        _blue(*args, end=end)
    elif verbose == 'MAGENTA':
        _magenta(*args, end=end)
    elif verbose == 'CYAN':
        _cyan(*args, end=end)


def _info(*args, end='\n'):
    _print(*args, end=end, header=vcolors.INFO, footer=tformat.ENDC)


def _warn(*args, end='\n'):
    _print(*args, end=end, header=vcolors.WARNING, footer=tformat.ENDC)


def _error(*args, end='\n'):
    _print(*args, end=end, header=vcolors.ERROR, footer=tformat.ENDC)


def _critical(*args, end='\n'):
    _print(*args, end=end, header=vcolors.CRITICAL, footer=tformat.ENDC)


def _red(*args, end='\n'):
    _print(*args, end=end, header=tcolors.FG_RED, footer=tformat.ENDC)


def _green(*args, end='\n'):
    _print(*args, end=end, header=tcolors.FG_GREEN, footer=tformat.ENDC)


def _yellow(*args, end='\n'):
    _print(*args, end=end, header=tcolors.FG_YELLOW, footer=tformat.ENDC)


def _blue(*args, end='\n'):
    _print(*args, end=end, header=tcolors.FG_BLUE, footer=tformat.ENDC)


def _magenta(*args, end='\n'):
    _print(*args, end=end, header=tcolors.FG_MAGENTA, footer=tformat.ENDC)


def _cyan(*args, end='\n'):
    _print(*args, end=end, header=tcolors.FG_CYAN, footer=tformat.ENDC)


def _print(*args, end='\n', header='', footer='', symbol='>'):
    msg = symbol*2 +' '+str(datetime.datetime.now()).split('.')[0][2:].replace(':', '.') + ':'
    for s in args:
        msg = msg + ' ' + str(s)
    print(header + msg + footer, end=end)


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


def cli_args(cli_params, usage=None):
    """Simple commad-line arguments built on top of argparse

    Parameters
    ----------
    cli_params : dict
        A python dict containing, cli argument name and defalut value as key, value pairs
    usage : str, optional
        Define custom usage (e.g. `'python main.py -a 0 -b 1.5 -c sky'`), by default None

    Returns
    -------
    dict
        A python dict similar to the input, except the values are replaced by user argument values

    Raises
    ------
    TypeError
        Input type can only be dict

    Usage
    -----
        # Normal usage
        cli_params = dict(
            task=0,
            factor=0.5,
            name='skylynx'
        )

        args = cli_args(cli_params)

        task = int(args['task'])
        factor = float(args['factor'])
        name = args['name']

        # Custom usage string
        usage = 'python tests/test.py -a 1'
        args = cli_args(cli_params, usage=usage)
    """

    params = _arg_reform(cli_params)
    # check if params is dict
    if isinstance(params, dict):
        parser = argparse.ArgumentParser(
            description='*** Simple cli args - by Skylynx ***', usage=usage)
        for key, value in params.items():
            parser.add_argument('-'+key, help=value[0], default=value[1])
        output = dict()

        for key1, key2 in dict(zip(cli_params, sorted(parser.parse_args().__dict__))).items():
            output[key1] = parser.parse_args().__dict__[key2]
        return output
    else:
        raise TypeError('params should be dict')


def makedirs(path):
    """Make directories if they do not already exists

    Parameters
    ----------
    path : str
        path/to/the/folder/
    """

    if not os.path.exists(path):
        os.makedirs(path)


def pprint(input, header=''):
    """Skylynx Pretty Print - Print a python dict object in a human readable form

    Parameters
    ----------
    input : dict
        Python dictionary
    header : str, optional
        Header for pretty print, by default ' '
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
    """Write .yml files

    Parameters
    ----------
    filename : .yml
        path/to/file/name.yml
    data : dict
        Python dictionary object
    """
    with open(filename, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


def yaml_read(filename):
    """Read .yml files

    Parameters
    ----------
    filename : .yml
        path/to/file/name.yml

    Returns
    -------
    dict
        Python dictionary object
    """
    with open(filename) as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def json_write(filename, data):
    """Write .json files (with indent and `utf-8` encoding)

    Parameters
    ----------
    filename : .json
        path/to/file/name.json
    data : dict
        Python dictionary object
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)


def json_read(filename):
    """Read .json files

    Parameters
    ----------
    filename : .json
        path/to/file/name.json

    Returns
    -------
    dict
        Python dictionary object
    """

    with open(filename) as f_in:
        return json.load(f_in)


if __name__ == '__main__':
    pass
