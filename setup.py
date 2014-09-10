#/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)
setup(
    name="furozun",
    version="0.0.1",
    description="Simple static site generator.",
    author="Amar Šahinović",
    author_email="amar@sahinovic.com",
    url="https://github.com/amarsahinovic/furozun",
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'],
    entry_points = {
        'console_scripts': [
            'furozun = furozun.main:main'
        ]
    },
    dependency_links=[
        'https://github.com/SimonSapin/Flask-FlatPages/archive/master.zip#egg=Flask-FlatPages'
    ],
    install_requires=[
        'Flask==0.10.1',
        'Flask-FlatPages',
        'Frozen-Flask==0.11',
        'Jinja2==2.7.3',
        'Markdown==2.4.1',
        'MarkupSafe==0.23',
        'PyYAML==3.11',
        'Pygments==1.6',
        'Werkzeug==0.9.6',
        'itsdangerous==0.24',
    ],
)
