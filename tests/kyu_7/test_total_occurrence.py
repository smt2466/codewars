# coding=utf-8
# pylint: disable=missing-docstring,redefined-outer-name,invalid-name

""""
Method For Counting Total occurrence Of Specific Digits
"""

import pytest

from src.kyu_7.total_occurrence import List


@pytest.fixture
def list_instance():
    return List()


def test_single_digit_number_list(list_instance):
    int_list = [1, 1, 2, 3, 1, 2, 3, 4]
    digit_list = [1, 3]
    answer = [(1, 3), (3, 2)]
    assert list_instance.count_spec_digits(int_list, digit_list) == answer


def test_negative_and_multi_digit_number_list(list_instance):
    int_list = [-18, -31, 81, -19, 111, -888]
    digit_list = [1, 8, 4]
    answer = [(1, 7), (8, 5), (4, 0)]
    assert list_instance.count_spec_digits(int_list, digit_list) == answer


def test_four_digit_number_list(list_instance):
    int_list = [-77, -65, 56, -79, 6666, 222]
    digit_list = [1, 8, 4]
    answer = [(1, 0), (8, 0), (4, 0)]
    assert list_instance.count_spec_digits(int_list, digit_list) == answer


def test_empty_list(list_instance):
    int_list = []
    digit_list = [1, 8, 4]
    answer = [(1, 0), (8, 0), (4, 0)]
    assert list_instance.count_spec_digits(int_list, digit_list) == answer
