# pylint: disable=missing-docstring, invalid-name

"""Unique In Order"""

from src.unique_in_order import unique_in_order


def test_string_upper_case():
    assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']


def test_string_with_lower_and_upper_case():
    assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']


def test_list_of_numbers():
    assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]


def test_empty_array():
    assert unique_in_order([]) == []
