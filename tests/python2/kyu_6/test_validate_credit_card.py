# pylint: disable=missing-docstring

"""Validate Credit Card Number"""

import pytest

from src.python2.kyu_6.validate_credit_card import validate

EXAMPLES = (
    ('card_num', 'expected'),
    [
        (123, False),
        (1, False),
        (2121, True),
        (1230, True),
        (8675309, False),
        (4111111111111111, True),
        (26, True),
        (2626262626262626, True),
        (91, True),
        (92, False)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(card_num, expected):
    assert validate(card_num) == expected
