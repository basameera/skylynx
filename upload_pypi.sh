#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo
    echo "Need Version (same as setup.py file)>>    bash upload_pypi.sh 'v0.0.1'"
    echo
    exit 1
fi

# upload to pypi
twine upload --repository pypi dist/$1/*
