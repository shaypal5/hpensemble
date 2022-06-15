"""Setup file for the hpensem package."""

# This file is part of hpensem.
# https://github.com/shaypal5/hpensem

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Shay Palachy <shaypal5@gmail.com>

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import versioneer


INSTALL_REQUIRES = [
]

TEST_REQUIRES = [
    # tests and coverages
    'pytest', 'coverage', 'pytest-cov',
    # to be able to run `python setup.py checkdocs`
    'collective.checkdocs', 'pygments',
]

README_RST = ''
with open('README.rst') as f:
    README_RST = f.read()


setup(
    name='hpensem',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=('A simple experiment'),
    long_description=README_RST,
    license='MIT',
    author='Shay Palachy',
    author_email='shay.palachy@gmail.com',
    url='https://github.com/shaypal5/hpensem',
    packages=['hpensem'],
    entry_points='''
        [console_scripts]
        hpensem=hpensem.scripts.cli:cli
    ''',
    install_requires=[
    ],
    extras_require={
        'test': TEST_REQUIRES,
    },
    platforms=['linux', 'osx', 'windows'],
    keywords=[],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Other/Nonlisted Topic',
        'Intended Audience :: Developers',
    ],
)
