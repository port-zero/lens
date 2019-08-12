#!/usr/bin/env python
import os
from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='lens-cli',
    author='Veit Heller',
    version='0.1.3',
    license='MIT',
    url='https://github.com/port-zero/lens',
    description='Extensible data structure traversal in the command line',
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url = 'https://github.com/port-zero/lens/tarball/0.1.3',
    packages=find_packages('.'),
    install_requires=[
        "pygments",
    ],
    entry_points={
        'console_scripts': [
            'lens = lens:run',
        ]
    },
)

