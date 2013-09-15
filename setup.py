"""
Setup file for packaging wordpress-py-client
"""

from setuptools import setup, find_packages

readme = open('README.md').read()
VERSION = '0.0.1'
REQUIREMENTS = {
	'install': ['httplib2', 'simplejson'],
	'testing': ['pytest', 'coverage', 'pytest-cov', 'python-coveralls'],
}

if __name__ == '__main__':
	setup(
	    version=VERSION,
	    name="wordpress-py-client",
	    description="A WordPress client written in Python",
	    long_description=readme,
	    author="Craig Cook",
	    author_email="theboycook@gmail.com",
	    url="https://github.com/BoyCook/WordPressPYClient",
	    packages=find_packages(exclude=["test"]),
	    install_requires=REQUIREMENTS["install"],
		extras_require= { "testing":  REQUIREMENTS["testing"] }
	)
