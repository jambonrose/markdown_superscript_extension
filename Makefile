.PHONY: check clean description dist release test

test:
	nosetests --with-coverage --cover-package=mdx_superscript

tox:
	tox

description:
	rst2html.py DESCRIPTION.rst > description.html

check:
	python setup.py check

dist:
	python setup.py sdist --formats=gztar,zip bdist_wheel
	gpg --armor --detach-sign -u 5878672C -a dist/MarkdownSuperscript*.whl
	gpg --armor --detach-sign -u 5878672C -a dist/MarkdownSuperscript*.tar.gz
	gpg --armor --detach-sign -u 5878672C -a dist/MarkdownSuperscript*.zip

release:
	twine upload dist/*

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf .tox
	rm -rf build
	rm -rf dist
