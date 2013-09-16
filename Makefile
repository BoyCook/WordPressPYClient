# Simple Makefile for some common tasks.
.PHONY: test dist upload

clean:
	find . -name "*.pyc" |xargs rm || true
	rm -r dist || true
	rm -r build || true
	rm -r *.egg-info || true
	rm tiddlyweb.log || true
	rm -r htmlcov || true
	rm .coverage || true	

clean-store:
	rm -r store || true

test:
	py.test -x -s test

test-cov:
	py.test --cov-report term-missing --cov wordpress test

test-cov-html:
	py.test --cov-report html --cov wordpress test

install:
	python setup.py install

dist:
	python setup.py sdist

release: clean pypi

pypi:
	python setup.py sdist upload
