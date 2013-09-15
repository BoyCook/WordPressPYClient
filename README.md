[![Build Status](https://travis-ci.org/BoyCook/WordPressPYClient.png)](https://travis-ci.org/BoyCook/WordPressPYClient)

## Description
A WordPress client written in Python

## Usage

    var blog = new WordPress(config);
	blog.getPosts();
	blog.getPost();


## Support

See http://developer.wordpress.com/docs/api

## Building

`setup.py` is used to package up the plugin, install and distribute.

* `make install` installs the plugin as a package on your system
* `make test` runs the tests.
* `make clean` cleans.
* `make release` packages and uploads the plugin to [PyPI](http://pypi.python.org/pypi) for distribution.
