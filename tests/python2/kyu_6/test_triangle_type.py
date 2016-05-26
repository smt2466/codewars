# pylint: disable=missing-docstring, invalid-name

"""Triangle type"""

from python2.kyu_6.triangle_type import triangle_type


def test_not_triangle_a_is_too_long():
    assert triangle_type(7, 3, 2) == 0


def test_not_triangle_a_is_equal_to_sum_b_c():
    assert triangle_type(6, 2, 4) == 0


def test_acute():
    assert triangle_type(8, 5, 7) == 1


def test_right():
    assert triangle_type(3, 4, 5) == 2


def test_obtuse():
    assert triangle_type(7, 12, 8) == 3
