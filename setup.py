# -*- coding: utf-8 -*-

from setuptools import setup

from skylynx import __version__, __author__, __author_email__


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


# setup(name='skylynx',
#       version=__version__,
#       description='Python support functions package',
#       long_description=readme(),
#       long_description_content_type="text/markdown",
#       url='https://github.com/basameera/skylynx',
#       author=__author__,
#       author_email=__author_email__,
#       license="MIT",
#       classifiers=[
#           "License :: OSI Approved :: MIT License",
#           "Programming Language :: Python :: 3",
#           "Programming Language :: Python :: 3.6",
#           "Programming Language :: Python :: 3.7",
#           "Programming Language :: Python :: 3.8",
#       ],
#       packages=["skylynx"],
#       include_package_data=True,
#       python_requires='>=3.6',
#       # install_requires=["requests"],
#       # entry_points={
#       #     "console_scripts": [
#       #         "weather-reporter=weather_reporter.cli:main",
#       #     ]
#       # },
#       )
