
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='rasam',
    version='0.3.0',
    description='Rasa Improved',
    python_requires='<3.8,>=3.6',
    author='Ronie Martinez',
    author_email='ronmarti18@gmail.com',
    license='MIT',
    keywords='URL extractor for Rasa Regex entity extractor for Rasa Placeholder importer for Rasa',
    classifiers=['Development Status :: 3 - Alpha', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: Implementation :: CPython'],
    packages=['rasam'],
    package_dir={"": "."},
    package_data={},
    install_requires=['faker==4.*,>=4.0.3', 'rasa==1.*,>=1.9.5', 'urlextract==0.*,>=0.14.0'],
    extras_require={"dev": ["asynctest==0.*,>=0.13.0", "autoflake==1.*,>=1.3.1", "black==19.*,>=19.10.0", "codecov==2.*,>=2.0.22", "dephell==0.*,>=0.8.2", "flake8==3.*,>=3.7.9", "isort==4.*,>=4.3.21", "mypy==0.*,>=0.770.0", "pytest==5.*,>=5.4.1", "pytest-asyncio==0.*,>=0.10.0", "pytest-cov==2.*,>=2.8.1"]},
)
