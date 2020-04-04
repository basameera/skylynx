import setup_path
import skylynx.utils as su
import os

if __name__ == "__main__":

    # Pretty Print
    data_dict = dict(
        a='This print a python dict object in a human readable form.',
        b=456,
        c=dict(
            d=123,
            e='skylynx'
        ),
        f = ['abc', 123]
    )
    su.pprint(data_dict, '> Header <')

    # Make Directories
    path = 'path/to/the/folder/'
    su.makedirs(path)
    print(os.path.exists(path))
    os.removedirs(path)
