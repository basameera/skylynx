#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo
    echo "Need Version (same as setup.py file)>>    bash upload_testpypi.sh 'v0.0.1'"
    echo
    exit 1
fi

# upload to testpypi
twine upload --repository testpypi dist/$1/*
