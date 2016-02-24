# coding=utf-8
# pylint: disable=missing-docstring,invalid-name,unidiomatic-typecheck
# pylint: disable=redefined-outer-name

"""
80's Kids #2: Help ALF Find His Spaceship
"""

import pytest

from src.kids_80s_2 import find_spaceship


@pytest.fixture
def lost_forever():
    return 'Spaceship lost forever.'


def test_expected_return_value_is_list_if_finding_is_possible():
    assert type(find_spaceship('X')) == list


def test_expected_return_value_is_str_if_finding_is_not_possible():
    assert type(find_spaceship('')) == str


def test_one_place():
    assert find_spaceship('X') == [0, 0]


def test_top():
    assert find_spaceship('X\n.') == [0, 1]


def test_top_right():
    assert find_spaceship('.X\n..') == [1, 1]


def test_bottom_right():
    assert find_spaceship('..\n.X') == [1, 0]


def test_bottom_left():
    assert find_spaceship('..\nX.') == [0, 0]


def test_bottom_left_wide_space():
    assert find_spaceship('.......\nX.......') == [0, 0]


def test_random_position_1():
    space = '..........\n' \
            '..........\n' \
            '.......X..\n' \
            '..........\n' \
            '..........'
    assert find_spaceship(space) == [7, 2]


def test_random_position_2():
    space = '..........\n' \
            '..........\n' \
            '..........\n' \
            '........X.\n' \
            '..........'
    assert find_spaceship(space) == [8, 1]


def test_no_ship_long_line(lost_forever):
    assert find_spaceship('........................') == lost_forever


def test_no_ship_long_column(lost_forever):
    assert find_spaceship('\n\n\n\n') == lost_forever
