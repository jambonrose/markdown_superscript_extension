Welcome to Markdown Superscript's documentation!
================================================

This Python package is an extension to the `Python Markdown`_ project
which adds the ability to superscript text. To do so, the character
:code:`~` becomes a Markdown tag for text meant to be superscripted, and
is replaced with the HTML :code:`sup` tag.

For example, the extension transforms the text directly below into the
HTML shown after it.

.. code-block:: text

    2^10^ is 1024.

.. code-block:: html

    <p>2<sup>10</sup> is 1024.</p>

The code is `Simplified (2 Clause) BSD license`_ and is available on `Github.`_

.. _`Python Markdown`: https://pypi.org/project/Markdown/
.. _`Simplified (2 Clause) BSD license`: https://choosealicense.com/licenses/bsd-2-clause/
.. _`Github.`: https://github.com/jambonrose/markdown_superscript_extension

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   contributing
   release
   authors
   history
