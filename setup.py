#!/usr/bin/env python
import os

from gitolite_manager import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

setup(
    name='gitolite-manager',
    version=__version__,
    description="Manage gitolite's configuration files and ssh keys",
    long_description=long_description,
    url='https://github.com/smailq/gitolite-manager',
    download_url=('https://github.com/downloads/smailq/gitolite-manager/'
                  'gitolite-manager-%s.tar.gz' % __version__),
    author='Kyu Lee',
    author_email='smailq@gmail.com',
    maintainer='Kyu Lee',
    maintainer_email='smailq@gmail.com',
    keywords=['Gitolite', 'gitolite management'],
    license='MIT',
    packages=['gitolite_manager'],
    test_suite='tests.all_tests',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
        ]
)
