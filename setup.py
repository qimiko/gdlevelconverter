"""
Setup script for pip
"""

from setuptools import setup, find_packages

setup(
    name='gdlevelconverter',
    version='1.0',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['gd-level-converter=gdlevelconverter.command_line:_main']
    },
    author='zmx',
    description='2.0+ to 1.9 Geometry Dash level conversion tool',
    install_requires=[
        "setuptools"
    ],
)
