#!/usr/bin/env python
import os
from setuptools import setup, find_packages

longdescr = open(
    os.path.join(
        os.path.dirname(__file__),
        'README.md'
    )
).read()


setup(
    name='lens',
    author='Veit Heller',
    version='0.0.1',
    license='MIT',
    url='https://github.com/port-zero/lens',
    description='Extensible data structure traversal in the command line',
    long_description=longdescr,
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'lens = lens:run',
        ]
    },
)

