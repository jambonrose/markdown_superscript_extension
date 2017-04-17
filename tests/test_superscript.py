# -*- coding: utf-8 -*-
"""
====================================
Markdown Superscript Extension Tests
====================================

:website: https://github.com/jambonrose/markdown_superscript_extension
:copyright: Copyright 2014-2017 Andrew Pinkham
:license: BSD, see LICENSE for details.
"""

from __future__ import unicode_literals
import unittest
from markdown import markdown


class SuperscriptTest(unittest.TestCase):
    """Basic functional tests for correct extension behavior."""

    def test_simple_string(self):
        """Basic use case."""
        text = "2^10^ is 1024."
        expected = "<p>2<sup>10</sup> is 1024.</p>"
        result = markdown(text, ['superscript'])
        self.assertEqual(expected, result)

    def test_multiple(self):
        """Test mutliple matches."""
        text = "2^10^ greater than 2^9^."
        expected = "<p>2<sup>10</sup> greater than 2<sup>9</sup>.</p>"
        result = markdown(text, ['superscript'])
        self.assertEqual(expected, result)
