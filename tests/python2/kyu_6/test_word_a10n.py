# pylint: disable=missing-docstring

"""Word a10n (abbreviation)"""

import pytest

from src.python2.kyu_6.word_a10n import abbreviate

EXAMPLES = (
    ('text', 'expected'),
    [
        ('internationalization', 'i18n'),
        ('accessibility', 'a11y'),
        ('Accessibility', 'A11y'),
        ('mat: is, balloon: cat. ', 'mat: is, b5n: cat. ')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert abbreviate(text) == expected
