# pylint: disable=missing-docstring

"""Number of permutations without repetitions"""

import pytest

from python2.src.kyu_6.permutations_without_repetition import perms

EXAMPLES = (
    ('element', 'expected'),
    [
        (2, 1),
        (25, 2),
        (342, 6),
        (1397, 24),
        (76853, 120),
        ('a', 1),
        ('ab', 2),
        ('abc', 6),
        (737, 3),
        (66666, 1)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(element, expected):
    assert perms(element) == expected
