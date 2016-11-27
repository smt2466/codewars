# pylint: disable=missing-docstring

"""For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre"""

import pytest

from python3.kyu_8.for_ufc_fans_total_beginners_conor_mcgregor_vs_george_saint_pierre import quote

EXAMPLES = (
    ('fighter', 'expected'),
    [
        ('george saint pierre', "I am not impressed by your performance."),
        ('conor mcgregor', "I'd like to take this chance to apologize.. "
                           "To absolutely NOBODY!"),
        ('Conor McGregor', "I'd like to take this chance to apologize.. "
                           "To absolutely NOBODY!")
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(fighter, expected):
    assert quote(fighter) == expected
