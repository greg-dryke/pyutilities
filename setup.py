# -*- coding: utf-8 -*-
import os
from setuptools import setup

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        return ''

setup(
    name='pyutils',
    version='0.0.1',
    packages=['pyutils'],
    author='Greg Dryke',
    author_email='greg.dryke@gmail.com',
    license='MIT',
    description='Random utilites for python projects',
    long_description = read('README.md'),
    install_requires=[
    ],
    # see here for complete list of classifiers
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ),
)
