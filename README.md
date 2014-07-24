[![Build Status](https://travis-ci.org/jambonrose/markdown_superscript_extension.svg?branch=master)](https://travis-ci.org/jambonrose/markdown_superscript_extension)

# Python Markdown Extension: Superscript

An extension to [Waylan Limberg](https://github.com/waylan)'s [Python Markdown](https://github.com/waylan/Python-Markdown) project ([documentation here](https://pythonhosted.org/Markdown/index.html)).

The goal of the extension is to provide support for basic superscript text in Markdown. To do so, the character `^` becomes a Markdown tag for text meant to be superscripted, and is replaced with the HTML `sup` tag.

For example, given the text: `2^10^ is 1024.`, using `Python Markdown` with this extension will output output `<p>2<sup>10</sup> is 1024.</p>`.
