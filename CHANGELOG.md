# Skylynx Changelog

This changelog summarizes major changes in `skylynx` python module.

## Version 0.1.2

#### Fixed

* `cli_args` usage

#### Added

* `docs/server.sh` for testing html docs
* `cli_args` custom usage
```python
cli_params = dict(
    task=0,
)

usage = 'python tests/test.py -a 1'

args = cli_args(cli_params, usage=usage)

task = int(args['task'])
```

```
$ python tests/test.py -h
usage: python tests/test.py -a 1

*** Simple cli args - by Skylynx ***

optional arguments:
  -h, --help  show this help message and exit
  -a A        task (default: 0)
```