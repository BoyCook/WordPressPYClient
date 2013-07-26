from setuptools import setup, find_packages

readme = open('README.md').read()
VERSION = '0.0.1'

setup(
    version=VERSION,
    name="wordpress-py-client",
    description="A WordPress client written in Python",
    long_description=readme,
    author="Craig Cook",
    url="https://github.com/BoyCook/WordPressPYClient",
    packages=find_packages(exclude=['test'])
)
