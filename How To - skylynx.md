# How to handle this Project - skylynx

## Module development workflow

1. Implementation
1. Testing
1. Unittest (if possible) (Travis-CI )
1. Update version (v0.1.2) in `__init__.py`
1. Gen Docs (Run `gen_docs.sh`)
1. Git push
1. Make `requirements.txt` (Run `bash pipreqs.sh`)
1. Switch to `master` branch and Push to PyPi (run `bash upload_pypi.sh v0.0.1`)

## requirements.txt

1. Run `bash pipreqs.sh`. This will create the proper `requirements.txt` file.

## To Do List

- [x] Add Change log
- [x] Generate docs

## Release

Only submit to PyPi through master branch



## Docs

1. Run `gen_docs.sh`
1. Put how to use info in `docs/USAGE.md`