# pylint: disable=missing-docstring

"""Fibonacci Reloaded"""

import pytest

from python3.kyu_6.fibonacci_reloaded import fib
from .test_nth_fibonacci import EXAMPLES


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, expected):
    assert fib(num) == expected
