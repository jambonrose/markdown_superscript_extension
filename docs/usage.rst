=====
Usage
=====

.. contents::
    :local:

Python
------

.. code-block:: pycon

    >>> from markdown import markdown
    >>> from mdx_superscript import SuperscriptExtension
    >>> text = "2^10^ is 1024."
    >>> markdown(text, extensions=[SuperscriptExtension()])
    '<p>2<sup>10</sup> is 1024.</p>'

You may also refer to the extension by module name or short module name.

.. code-block:: pycon

    >>> markdown(text, extensions=['mdx_superscript'])
    >>> markdown(text, extensions=['superscript'])

.. NOTE::
    In older versions of Markdown, you will need to refer to the module
    without the ``mdx`` prefix (the second line of code above).

Command Line
------------

.. code-block:: console

    $ echo '2^10^ is 1024.' > text.md
    $ python -m markdown -o html -x 'mdx_superscript' -f text.html text.md
    $ cat text.html
    <p>2<sup>10</sup> is 1024.</p>
