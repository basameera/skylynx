#!/bin/bash
# generate requirements.txt
echo 
echo ===== piprequire =====

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo Generating $DIR/requirements.txt

pipreqs --force --savepath pipreqs.txt $DIR

python import_handler.py

rm pipreqs.txt