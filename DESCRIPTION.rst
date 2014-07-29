An extension to the `Python Markdown`_ project which adds the ability to superscript text. To do so, the character :code:`^` becomes a Markdown tag for text meant to be superscripted, and is replaced with the HTML :code:`sup` tag.

For example, given the text: ::

    2^10^ is 1024.

… using Markdown with this extension will output: ::

    <p>2<sup>10</sup> is 1024.</p>

This project is provided under the `Simplified (2 Clause) BSD license`_.

Installation
------------

::

    pip install MarkdownSuperscript

Usage
-----

Python
^^^^^^

>>> from markdown import markdown
>>> text = "2^10^ is 1024."
>>> markdown(text, ['superscript'])
'<p>2<sup>10</sup> is 1024.</p>'

Command Line
^^^^^^^^^^^^

::

    $ echo '2^10^ is 1024.' > text.md
    $ python -m markdown -o html5 -x 'superscript' -f text.html text.md

.. _`Python Markdown`: https://pypi.python.org/pypi/Markdown
.. _`Simplified (2 Clause) BSD license`: http://choosealicense.com/licenses/bsd-2-clause/
