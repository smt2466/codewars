# pylint: disable=missing-docstring

"""Unary function chainer"""

import pytest

from python2.src.kyu_6.unary_function_chainer import chained


def func1(arg):
    return arg * 2


def func2(arg):
    return arg + 2


def func3(arg):
    return arg ** 2


def func4(arg):
    return arg.split()


def func5(arg):
    return [item[::-1].title() for item in arg]


def func6(arg):
    return "_".join(arg)

EXAMPLES = (
    ('functions', 'argument', 'expected'),
    [
        ([func1, func2, func3], 0, 4),
        ([func1, func2, func3], 2, 36),
        ([func3, func2, func1], 2, 12),
        ([func4, func5, func6], 'lorem ipsum dolor', 'Merol_Muspi_Rolod')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(functions, argument, expected):
    assert chained(functions)(argument) == expected
