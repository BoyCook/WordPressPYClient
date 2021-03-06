[![Build Status](https://travis-ci.org/BoyCook/WordPressPYClient.png)](https://travis-ci.org/BoyCook/WordPressPYClient)
[![Coverage Status](https://coveralls.io/repos/BoyCook/WordPressPYClient/badge.png)](https://coveralls.io/r/BoyCook/WordPressPYClient)
[![Version](https://pypip.in/v/wordpress-py-client/badge.png)](https://crate.io/packages/wordpress-py-client)
[![Downloads](https://pypip.in/d/wordpress-py-client/badge.png)](https://crate.io/packages/wordpress-py-client)

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
