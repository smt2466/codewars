# pylint: disable=missing-docstring

"""Module docstring"""

from python2.kyu_6.polybius_square_cipher import polybius


def test_one_word():
    assert polybius('CODEWARS') == '1334141552114243'


def test_multiple_words():
    answer = '3534315412244543 434145114215 132435231542'
    assert polybius('POLYBIUS SQUARE CIPHER') == answer
