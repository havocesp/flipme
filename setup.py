#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Flyp.me

File: /setup.py
Author: Havocesp <https://github.com/havocesp/Flyp.me>
Created: 2022-05-24
"""
from setuptools import find_packages, setup

setup(
    name='flipme',
    version='0.0.1',
    # packages=['flipme'],,
    packages=find_packages(exclude=['.idea*', 'build*', f'{__package__}.egg-info*', 'dist*', 'venv*']),
    url=f'https://github.com/havocesp/{__package__}',
    license='UNLICENSE',
    packages_dir={'': __package__},
    # keywords=__keywords__,
    author='HavocESP',
    author_email='umpierrez@pm.me',
    long_description='',
    description='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires='Flip.me site API wraper.'
)
