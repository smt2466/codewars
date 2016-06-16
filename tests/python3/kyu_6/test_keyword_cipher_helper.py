# pylint: disable=invalid-name, missing-docstring, redefined-outer-name

"""Keyword Cipher Helper"""

import pytest

from python3.kyu_6.keyword_cipher_helper import keyword_cipher

ENCODE = (
    ('text', 'expected'),
    [
        ('abc', 'key'),
        ('xyz', 'vxz'),
    ]
)

DECODE = (
    ('text', 'expected'),
    [
        ('key', 'abc'),
        ('vxz', 'xyz'),
    ]
)


@pytest.fixture
def cipher():
    abc = 'abcdefghijklmnopqrstuvwxyz'
    key = 'keyword'
    return keyword_cipher(abc, key)


@pytest.mark.parametrize(*ENCODE)
def test_encode_returns_correct_result(text, expected, cipher):
    assert cipher.encode(text) == expected


@pytest.mark.parametrize(*DECODE)
def test_decode_returns_correct_result(text, expected, cipher):
    assert cipher.decode(text) == expected
