# pylint: disable=missing-docstring, invalid-name

"""Function iteration"""

from src.kyu_6.function_iteration import create_iterator


def get_double(num):
    return 2*num

double_iterator = create_iterator(get_double, 1)
get_quadruple = create_iterator(get_double, 2)


def test_run_once():
    assert double_iterator(3) == 6
    assert double_iterator(5) == 10


def test_run_twice():
    assert get_quadruple(2) == 8
    assert get_quadruple(5) == 20

