.. image:: https://travis-ci.org/BoyCook/WordPressPYClient.png
    :target: https://travis-ci.org/BoyCook/WordPressPYClient
    :alt: Build Status
.. image:: https://coveralls.io/repos/BoyCook/WordPressPYClient/badge.png
    :target: https://coveralls.io/r/BoyCook/WordPressPYClient
    :alt: Coverage Status
.. image:: https://pypip.in/v/wordpress-py-client/badge.png
    :target: https://crate.io/packages/wordpress-py-client
    :alt: Package Version
.. image:: https://pypip.in/d/wordpress-py-client/badge.png
    :target: https://crate.io/packages/wordpress-py-client
    :alt: Package Downloads

Description
===========

A WordPress client written in Python

Usage
=====

    var blog = new WordPress(config);
	blog.getPosts();
	blog.getPost();

Support
=======

See http://developer.wordpress.com/docs/api

Building
========

`setup.py` is used to package up the plugin, install and distribute.

* `make install` installs the plugin as a package on your system
* `make test` runs the tests.
* `make clean` cleans.
* `make release` packages and uploads the plugin to http://pypi.python.org/pypi for distribution.
