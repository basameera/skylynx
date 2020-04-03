# -*- coding: utf-8 -*-

from setuptools import setup

version = '0.0.1'

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(name='skylynx',
      version=version,
      description='Python package testing',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='https://github.com/basameera/skylynx',
      author='Sameera Sandaruwan',
      author_email='basameera@protonmail.com',
      license="MIT",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7",
      ],
      packages=["skylynx"],
      include_package_data=True,
      # install_requires=["requests"],
      # entry_points={
      #     "console_scripts": [
      #         "weather-reporter=weather_reporter.cli:main",
      #     ]
      # },
      )
