# pylint: disable=missing-docstring, redefined-outer-name

"""PaginationHelper"""

import pytest

from python2.kyu_5.paginationhelper import PaginationHelper


@pytest.fixture
def helper():
    return PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)


def test_should_have_two_pages(helper):
    assert helper.page_count() == 2


def test_should_have_six_items(helper):
    assert helper.item_count() == 6


def test_first_page_is_full(helper):
    assert helper.page_item_count(0) == 4


def test_second_page_is_half_full(helper):
    assert helper.page_item_count(1) == 2


def test_third_page_is_empty(helper):
    assert helper.page_item_count(2) == -1


def test_correct_item_index_page(helper):
    assert helper.page_index(5) == 1
    assert helper.page_index(2) == 0


def test_invalid_item_index_page(helper):
    assert helper.page_index(20) == -1
    assert helper.page_index(-10) == -1
