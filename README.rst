Latest Release: |Version| |Tag|

Compatibility: |Implementation| |Python| |License|

Tests: |Build| |Coverage| |PyUp| |Requirements|

.. |Version| image:: http://img.shields.io/pypi/v/MarkdownSuperscript.svg
        :target: https://pypi.python.org/pypi/MarkdownSuperscript/
        :alt: PyPI Version

.. |Tag| image:: https://img.shields.io/github/tag/jambonrose/markdown_superscript_extension.svg
        :target: https://github.com/jambonrose/markdown_superscript_extension/releases
        :alt: Github Tag

.. |Implementation| image:: https://img.shields.io/pypi/implementation/MarkdownSuperscript.svg
        :target: https://pypi.python.org/pypi/MarkdownSuperscript/
        :alt: Python Implementation Support

.. |Python| image:: https://img.shields.io/pypi/pyversions/MarkdownSuperscript.svg
        :target: https://pypi.python.org/pypi/MarkdownSuperscript/
        :alt: Python Support

.. |License| image:: http://img.shields.io/pypi/l/MarkdownSuperscript.svg
        :target: http://opensource.org/licenses/BSD-2-Clause
        :alt: License

.. |Build| image:: https://travis-ci.org/jambonrose/markdown_superscript_extension.svg?branch=development
        :target: https://travis-ci.org/jambonrose/markdown_superscript_extension
        :alt: Build Status

.. |Coverage| image:: https://codecov.io/gh/jambonrose/markdown_superscript_extension/branch/development/graph/badge.svg
        :target: https://codecov.io/gh/jambonrose/markdown_superscript_extension
        :alt: Coverage Status

.. |PyUp| image:: https://pyup.io/repos/github/jambonrose/markdown_superscript_extension/shield.svg
        :target: https://pyup.io/repos/github/jambonrose/markdown_superscript_extension/
        :alt: Updates

.. |Requirements| image:: https://requires.io/github/jambonrose/markdown_superscript_extension/requirements.svg?branch=development
        :target: https://requires.io/github/jambonrose/markdown_superscript_extension/requirements/?branch=development
        :alt: Requirements Status

=======
Read Me
=======

An extension to the `Python Markdown`_ project which adds the ability to
superscript text. To do so, the character :code:`^` becomes a Markdown
tag for text meant to be superscripted, and is replaced with the HTML
:code:`sup` tag.

For example, given the text: ::

    2^10^ is 1024.

… using Markdown with this extension will output:

.. code :: html

    <p>2<sup>10</sup> is 1024.</p>

This project is provided under the `Simplified (2 Clause) BSD license`_,
provided in full in the LICENSE file.

.. _`Python Markdown`: https://pypi.python.org/pypi/Markdown
.. _`Simplified (2 Clause) BSD license`: http://choosealicense.com/licenses/bsd-2-clause/

Installation
------------

Dependencies:

- Python 2.7, 3.3+

- Markdown 2.5+
  (Tested against latest patch version of Markdown 2.5, 2.6, 3.0)

To install the latest stable release (recommended):

.. code :: bash

    pip install MarkdownSuperscript

To install the development version:

.. code :: bash

    pip install git+git://github.com/jambonrose/markdown_superscript_extension.git

Basic Usage
-----------

Python
^^^^^^

.. code :: pycon

    >>> from markdown import markdown
    >>> text = "2^10^ is 1024."
    >>> markdown(text, extensions=['mdx_superscript'])
    '<p>2<sup>10</sup> is 1024.</p>'

Command Line
^^^^^^^^^^^^

.. code :: bash

    $ echo '2^10^ is 1024.' > text.md
    $ python -m markdown -o html5 -x 'mdx_superscript' -f text.html text.md
