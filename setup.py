# hyphenate.py - hyphenate English words
#
# This file is part of Hyphenate. The authors of Hyphenate abandon all
# claims to copyright, and dedicate it to the public domain.
"""Hyphenate, using Frank Liang's algorithm.

This module provides a single function to hyphenate words. The
``hyphenate_word`` function takes a string (the word to hyphenate), and
returns a list of parts that can be separated by hyphens. For example::

    >>> from hyphenate import hyphenate_word
    >>> hyphenate_word('hyphenation')
    ['hy', 'phen', 'ation']
    >>> hyphenate_word('supercalifragilistic')
    ['su', 'per', 'cal', 'ifrag', 'ilis', 'tic']
    >>> hyphenate_word('project')
    ['project']

This code, originally written by Ned Batchelder in July 2007, is in the
public domain.

"""
import os
import re
from setuptools import setup

#: A regular expression capturing the version number from Python code.
VERSION_RE = r"^__version__ = ['\"]([^'\"]*)['\"]"


def find_version(path):
    """Find a version number in a given file.

    `path` is a string naming a path to a file relative to the directory
    containing *this* file. This function outputs a string representing
    a version number.

    Each positional argument indicates a member of the path.

    """
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, path), 'r') as f:
        version_file = f.read()
    version_match = re.search(VERSION_RE, version_file, re.MULTILINE)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    # Metadata
    name='Hyphenate',
    version=find_version('hyphenate.py'),
    url='https://github.com/jfinkels/hyphenate',
    download_url='https://pypi.python.org/pypi/hyphenate',
    author='Ned Batchelder',
    maintainer='Jeffrey Finkelstein',
    maintainer_email='jeffrey.finkelstein@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing',
    ],
    license='Public Domain',
    description='Determine hyphenation breaks in English words',
    long_description=__doc__,
    platforms='any',
    # Options
    py_modules=['hyphenate'],
    test_suite='test_hyphenate',
)
