# coding=utf-8
# pylint: disable=missing-docstring, invalid-name, redefined-outer-name

"""
String Shortener (shrink)
"""

import pytest

from src.kyu_6.string_shortener import shorten


@pytest.fixture
def sentence():
    return 'The quick brown fox jumps over the lazy dog'


@pytest.fixture
def hello_world():
    return 'hello world'


def test_default_glue_long_string(sentence):
    assert shorten(sentence, 27) == 'The quick br...the lazy dog'


def test_specific_glue_long_string(sentence):
    assert shorten(sentence, 27, '----') == 'The quick b----the lazy dog'


def test_default_glue_even_length(sentence):
    assert shorten(sentence, 20) == 'The quic... lazy dog'


def test_string_is_shorter_than_length(hello_world):
    assert shorten(hello_world, 20) == 'hello world'


def test_shorten_to_hard():
    assert shorten('hello', 5, '----') == 'hello'


def test_minimum_fit(hello_world):
    assert shorten(hello_world, 5, '---') == 'h---d'


def test_length_too_short_for_glue(hello_world):
    assert shorten(hello_world, 5, '----') == 'hello'
