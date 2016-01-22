#!/usr/bin/env python

from setuptools import setup
import sys
from codecs import open


def lines(text):
    """
    Returns each non-blank line in text enclosed in a list.
    See http://pypi.python.org/pypi/textdata for more sophisticated version.
    """
    return [l.strip() for l in text.strip().splitlines() if l.strip()]


setup(
    name='say',
    version='1.4.2',
    author='Jonathan Eunice',
    author_email='jonathan.eunice@gmail.com',
    description='print and format on steroids',
    long_description=open('README.rst', encoding='utf-8').read(),
    url='https://bitbucket.org/jeunice/say',
    license='Apache License 2.0',
    packages=['say'],
    setup_requires=[],
    install_requires=['six>=1.9', 'options>=1.4.0', 'simplere>=1.2.7',
                      'mementos>=1.2.0', 'ansicolors'],
    tests_require=['tox', 'pytest', 'six'],
    zip_safe=False,
    keywords='print format template interpolate say',
    classifiers=lines("""
        Development Status :: 5 - Production/Stable
        Operating System :: OS Independent
        License :: OSI Approved :: Apache Software License
        Intended Audience :: Developers
        Programming Language :: Python
        Programming Language :: Python :: 2
        Programming Language :: Python :: 2.6
        Programming Language :: Python :: 2.7
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.2
        Programming Language :: Python :: 3.3
        Programming Language :: Python :: 3.4
        Programming Language :: Python :: 3.5
        Programming Language :: Python :: Implementation :: CPython
        Programming Language :: Python :: Implementation :: PyPy
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: Printing
    """)
)
