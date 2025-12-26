from setuptools import setup

version = open("version.txt").read()[1:] #Gets the version number
readme = open("README.md").read() #Gets README.md


setup(
    name='metaerrors',
    version=version,
    packages=['metaerrors'],
    url='https://github.com/IgorNk500/metaerrors',
    license='GPL-3.0',
    author='IgorNk500',
    author_email='',
    description='Outputs exceptions in popups',
    long_description=readme,
    long_description_content_type="text/markdown"
)
