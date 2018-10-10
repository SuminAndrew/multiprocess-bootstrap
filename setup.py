# coding=utf-8

from setuptools import setup

setup(
    name='multiprocess-bootstrap',
    version='0.2.0',
    description='Runs several copies of a process and restarts them if they die. Useful in docker environments.',
    long_description='Runs several copies of a process and restarts them if they die. Useful in docker environments.',
    url='https://github.com/SuminAndrew/multiprocess-bootstrap',
    author='Andrew Sumin',
    author_email='sumin.andrew@gmail.com',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Testing',
    ],
    license="http://www.apache.org/licenses/LICENSE-2.0",
    packages=[],
    install_requires=[],
    scripts=['bootstrap.py'],
    zip_safe=False
)
