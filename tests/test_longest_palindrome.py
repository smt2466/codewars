# pylint: disable=missing-docstring, invalid-name

""""longest_palindrome"""

from src.longest_palindrome import longest_palindrome


def test_single_char():
    assert longest_palindrome('a') == 1


def test_two_equal_chars():
    assert longest_palindrome('aa') == 2


def test_palindrome_at_the_end_of_the_string():
    assert longest_palindrome('baa') == 2


def test_palindrome_at_the_start_of_the_string():
    assert longest_palindrome('aab') == 2


def test_no_palindrome():
    assert longest_palindrome('abcdefghba') == 1


def test_long_palindrome_inside_the_string():
    assert longest_palindrome('baablkj12345432133d') == 9


def test_empty_string():
    assert longest_palindrome('') == 0
