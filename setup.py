# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cad-it',
    version='0.1.0',
    description='CAD-IT Code Test',
    long_description=readme,
    author='nithya panniyan',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

