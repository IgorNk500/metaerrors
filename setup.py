from setuptools import setup

version = open("version.txt").read()[1:] #Gets the version number

setup(
    name='metaerrors',
    version=version,
    packages=['metaerrors'],
    url='https://github.com/IgorNk500/metaerrors',
    license='GPL-3.0',
    author='IgorNk500',
    author_email='https://github.com/IgorNk500',
    description='Outputs errors in popups'
)
