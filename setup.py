#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='omdb',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['requests'],
)
