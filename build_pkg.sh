#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo
    echo "Need Version (same as setup.py file)>>    bash build_pkg.sh 'v0.0.1'"
    echo
    exit 1
fi

# Build .tar.gz and .whl files
echo Building....
python setup.py sdist --dist-dir 'dist/'$1 bdist_wheel --dist-dir 'dist/'$1

# check the build files
echo
echo Checking build..
twine check dist/$1/*
