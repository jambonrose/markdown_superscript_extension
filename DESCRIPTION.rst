.. role:: html(code)
       :language: html

An extension to the `Python Markdown`_ project which adds the ability to superscript text. To do so, the character :code:`^` becomes a Markdown tag for text meant to be superscripted, and is replaced with the HTML :html:`sup` tag.

For example, given the text: :code:`2^10^ is 1024.`, using `Python Markdown`_ with this extension will output output :html:`<p>2<sup>10</sup> is 1024.</p>`.

.. _`Python Markdown`: https://pypi.python.org/pypi/Markdown

Usage
-----

>>> from markdown import markdown
>>> text = "2^10^ is 1024."
>>> markdown(text, ['superscript'])
'<p>2<sup>10</sup> is 1024.</p>'
