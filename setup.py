#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================================
Markdown Superscript Extension Distutils Setup
==============================================

:website: https://github.com/jambonrose/markdown_superscript_extension
:copyright: Copyright 2014 Andrew Pinkham
:license: Simplified BSD, see LICENSE for details.
"""

from setuptools import setup


long_description="""
.. role:: html(code)
       :language: latex

An extension to the `Python Markdown`_ project which adds the ability to superscript text. To do so, the character :code:`^` becomes a Markdown tag for text meant to be superscripted, and is replaced with the HTML :html:`sup` tag.

For example, given the text: :code:`2^10^ is 1024.`, using `Python Markdown`_ with this extension will output output :html:`<p>2<sup>10</sup> is 1024.</p>`.

.. _`Python Markdown`: https://pypi.python.org/pypi/Markdown

Usage
-----

>>> from markdown import markdown
>>> text = "2^10^ is 1024."
>>> markdown(text, ['superscript'])
'<p>2<sup>10</sup> is 1024.</p>'

"""


setup(
    name='Markdown Superscript',
    version='1.0b1', # PEP 386 Compliant Semantic Versioning
    description='Python-Markdown extension to allow for superscript text.',
    long_description=long_description,
    author='Andrew Pinkham',
    author_email='hello at andrewsforge dot com',
    url='https://github.com/jambonrose/markdown_superscript_extension',
    py_modules=['mdx_superscript'],
    install_requires=['Markdown>=2.0'],
    license = 'Simplified BSD License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
