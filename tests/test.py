
import os
import sys
sys.path.insert(0, os.getcwd())

import skylynx
import skylynx.utils as  su

if __name__ == "__main__":
    print('skylynx', skylynx.__version__)

    jdata = dict(a=123,b='skylynx')
    su.json_write('misc/test.json', jdata)
    data = su.json_read('misc/test.json')
    print(data)

    su.yaml_write('misc/test.yaml', jdata)
    data = su.yaml_read('misc/test.yaml')
    print(data)