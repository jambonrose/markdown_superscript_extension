# -*- coding: utf-8 -*-
"""Markdown Superscript Extension Tests

:website: https://github.com/jambonrose/markdown_superscript_extension
:copyright: Copyright 2014-2018 Andrew Pinkham
:license: BSD, see LICENSE for details.

"""
from __future__ import unicode_literals

from markdown import markdown, version_info as md_version
from mdx_superscript import SuperscriptExtension
from pytest import fixture, mark, param

TEXT_DATA_FIELDS = "markdown_text, expected_html"
TEXT_DATA = [
    param(
        "2^10^ is 1024.",
        "<p>2<sup>10</sup> is 1024.</p>",
        id="Simple substitution",
    ),
    param(
        "2^10^ greater than 2^9^.",
        "<p>2<sup>10</sup> greater than 2<sup>9</sup>.</p>",
        id="Multiple substitutions",
    ),
]


@fixture(
    scope="session",
    params=[
        param([SuperscriptExtension()], id="Direct Extension"),
        param(
            ["mdx_superscript"],
            marks=mark.skipif(
                md_version < (2, 6),
                reason="Module matching by full name added in Markdown 2.6",
            ),
            id="Full module name",
        ),
        param(["superscript"], id="Short module name"),
    ],
)
def extensions(request):
    """Parameterized Fixture for extensions kwarg of markdown"""
    return request.param


@mark.parametrize(TEXT_DATA_FIELDS, TEXT_DATA)
def test_superscript_extension(markdown_text, expected_html, extensions):
    """Test the superscript extensions

    PyTest parameterized arguments allow for multiple text inputs to be
    tested.

    The Markdown package allows for extensions to be requested in a
    number of ways. We use a PyTest parameterized fixture to test each
    of those methods.

    We are therefore testing multiple text inputs in multiple
    extension-loading scenarios.

    """
    result = markdown(markdown_text, extensions=extensions)
    assert result == expected_html
