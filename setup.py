"""This setuptools-based builder uses README.md, version.txt, and pylib.json files to build package metadata."""

import json
from setuptools import setup

print("Project info getting from README.md, version.txt and pylib.json")

version = open("version.txt").read()[1:-1] #Gets the version number
readme = open("README.md").read() #Gets README.md
info = json.load(open("pylib.json"))

setup(
    version=version,
    long_description=readme,
    long_description_content_type="text/markdown",
    **info
)
