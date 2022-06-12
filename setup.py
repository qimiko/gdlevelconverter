"""
Setup script for pip
"""

from setuptools import setup, find_packages

README_PATH = "README.md"

with open(README_PATH, "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='gdlevelconverter',
    version='1.0.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['gd-level-converter=gdlevelconverter.command_line:_main']
    },
    author='qimiko',
    description='2.0+ to 1.9 Geometry Dash level conversion tool',
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=[
        "setuptools"
    ],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3'
)
