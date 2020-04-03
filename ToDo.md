# How to

Refer https://truveris.github.io/articles/configuring-pypirc/

**NOTE:** Remove `.travis.yaml` before first git push

---

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

### Travis CI
1. Install `pip install pipreqs`
1. Run `bash pipreqs.sh`
1. First push the git **without** `.travis.yaml` file.
1. Then add the repository in Travis-CI
1. Add the `build status` markdown to the `README.md` file.
1. Then push git with `.travis.yaml` file. **NOTE:** content of `.travis.yaml` is below;
    ```
    language: python
    python:
    - "3.6"
    - "3.7" # current default Python on Travis CI
    - "3.8"
    cache: pip
    # command to install dependencies
    install:
    - pip install -r requirements.txt
    # command to run tests
    script:
    - python tests/test_basic.py
    ```

---

## Reference

### Python module structuring

https://python-packaging.readthedocs.io/en/latest/minimal.html
https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
https://docs.python-guide.org/writing/structure/

### Setup

Learn more: https://github.com/kennethreitz/setup.py

### Python packaging

https://packaging.python.org/tutorials/packaging-projects/
https://gist.github.com/nikhilkumarsingh/08a3ab33d1c3ad955fe3f88743aef322

https://python-packaging.readthedocs.io/en/latest/minimal.html#publishing-on-pypi

https://github.com/nikhilkumarsingh/weather-reporter
https://www.youtube.com/watch?v=RgfOjrjhCMY

### Twine

https://github.com/pypa/twine