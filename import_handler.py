"""
* Only run through `bash pipreqs.sh`
* Read `pipreqs.txt` and find the correct version and write to `requirements.txt`
"""
import skylynx
import os
import pkg_resources


def read_req():

    output_str = ''
    fname = 'pipreqs.txt'
    if os.path.isfile(fname):
        with open(fname) as f:
            content = f.readlines()
            for line in content:
                module = line.rstrip().split('==')[0]
                local_version = pkg_resources.get_distribution(module).version
                output_str += '{}>={}\n'.format(module, local_version)
    else:
        raise AttributeError(
            'No \'requirements.txt\' file. Please run \'bash pipreqs.sh\' to generate it.')

    with open('requirements.txt', 'w') as outfile:
        outfile.write(output_str)


if __name__ == "__main__":
    read_req()
