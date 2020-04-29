import setup_path
# import skylynx.utils as su
from skylynx.utils import cli_args, clog
import os

if __name__ == "__main__":
    cli_params = dict(
        task=0,
    )

    usage = 'python tests/test.py -a 1'

    args = cli_args(cli_params, usage=usage)

    task = int(args['task'])

    clog('Hello')
