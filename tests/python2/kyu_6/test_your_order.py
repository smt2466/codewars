# pylint: disable=missing-docstring

""""Your order, please"""

from python2.kyu_6.your_order import order


def test_return_correct_result():
    assert order('is2 Thi1s T4est 3a') == 'Thi1s is2 3a T4est'


def test_empty_string():
    assert order('') == ''
