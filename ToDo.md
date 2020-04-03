# How to

Refer https://truveris.github.io/articles/configuring-pypirc/

## 1. Package

Make package folder - skylynx

## 2. Tests

1. Make tests folder
2. Make `tests/test_basic.py` file
3. Run `python tests/test_basic.py`

## 3. Make `setup.py` 

Fill out `setup.py` properly

## 4. Build

1. Install **`twine`** - `pip install twine`
1. Make `testpypi` and `pypi` accounts
1. Setup `$HOME/.pypirc` file
    ``` 
    [distutils]
    index-servers=
        pypi
        testpypi

    [pypi]
    username: __token__
    password: API key starting with pypi-

    [testpypi]
    repository: https://test.pypi.org/legacy/
    username: __token__
    password: API key starting with pypi-
    ```
1. Secure the file : `chmod 600 ~/.pypirc`
1. Run `bash build_pkg.sh <version>` - (e.g. `bash build_pkg.sh 'v0.0.1'` )
1. Upload to **`testpypi`**: Run `bash upload_testpypi.sh <version>`
1. Upload to **`pypi`**: Run `bash upload_pypi.sh <version>`

## 5. CI/CD