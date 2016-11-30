#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='lens-cli',
    author='Veit Heller',
    version='0.1.2',
    license='MIT',
    url='https://github.com/port-zero/lens',
    description='Extensible data structure traversal in the command line',
    download_url = 'https://github.com/port-zero/lens/tarball/0.1.2',
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

