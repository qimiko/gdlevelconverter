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
	description='Geometry Dash level conversion tools',
	install_requires=[
		"setuptools"
	],
)
