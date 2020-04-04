import setup_path
# import skylynx.utils as su
from skylynx.utils import cli_args
import os

if __name__ == "__main__":

    # simple command line arguments
    cli_params = dict(task=0,
                      length=10
                      )

    args = cli_args(cli_params)
    task = args['task']
    length = args['length']
