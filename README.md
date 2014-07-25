# Python Markdown Extension: Superscript

[![Build Status](https://travis-ci.org/jambonrose/markdown_superscript_extension.svg?branch=master)](https://travis-ci.org/jambonrose/markdown_superscript_extension)

An extension to [Waylan Limberg](https://github.com/waylan)'s [Python Markdown](https://github.com/waylan/Python-Markdown) project ([documentation here](https://pythonhosted.org/Markdown/index.html)).

The goal of the extension is to provide support for basic superscript text in Markdown. To do so, the character `^` becomes a Markdown tag for text meant to be superscripted, and is replaced with the HTML `sup` tag.

For example, given the text: `2^10^ is 1024.`, using `Python Markdown` with this extension will output output `<p>2<sup>10</sup> is 1024.</p>`.

## Installation

Dependencies:

- Python 2.6, 2.7, 3.2+
- Markdown 2.0+

To install the development version:

    pip install git+git://github.com/jambonrose/markdown_superscript_extension.git

## Basic Usage

[Python Markdown](https://github.com/waylan/Python-Markdown) can be used in two ways:

1. directly in Python
2. via the command line

Extensions are accessible in both cases.

### Python

```python
>>> from markdown import markdown
>>> text = "2^10^ is 1024."
>>> markdown(text, ['superscript'])
'<p>2<sup>10</sup> is 1024.</p>'
```

### Command Line

```bash
$ echo '2^10^ is 1024.' > text.md
$ python -m markdown -o html5 -x 'superscript' -f text.html text.md
```
