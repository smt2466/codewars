# pylint: disable=missing-docstring

"""Is a number prime?"""

import pytest

from src.python2.kyu_6.is_prime import is_prime

EXAMPLES = (
    ('number', 'expected'),
    [
        (0, False),  # Zero
        (1, False),
        (2, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert is_prime(number) == expected
