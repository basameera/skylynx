# -*- coding: utf-8 -*-

from setuptools import setup
import os
from skylynx import __version__, __author__, __author_email__


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


def read_reqs():
    req_list = []
    fname = 'requirements.txt'
    if os.path.isfile(fname):
        with open(fname) as f:
            content = f.readlines()
            for line in content:
                req_list.append(line.rstrip())
    else:
        raise AttributeError(
            'No \'requirements.txt\' file. Please run \'bash pipreqs.sh\' to generate it.')

    return req_list


setup(name='skylynx',
      version=__version__,
      description='Python support functions package',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='https://github.com/basameera/skylynx',
      author=__author__,
      author_email=__author_email__,
      license="MIT",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
      ],
      packages=["skylynx"],
      include_package_data=True,
      python_requires='>=3.6',
      install_requires=read_reqs(),
      # entry_points={
      #     "console_scripts": [
      #         "weather-reporter=weather_reporter.cli:main",
      #     ]
      # },
      )
