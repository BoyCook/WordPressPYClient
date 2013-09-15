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
    packages=find_packages(exclude=["test"]),
    "install_requires": ["setuptools",
    "httpexceptor>=1.2.0",
    # modern Selector requires modern Python, so downgrade for older versions
    "selector" + ("<0.9.0" if (sys.version_info[0] == 2 and
            sys.version_info[1] < 6) else ""),
    "simplejson",
    "html5lib<0.96",
    "mimeparse"],
	"extras_require": {
    	"testing": 
    		["pytest", "httplib2", "coverage","pytest-cov", "python-coveralls"]
		}
)
