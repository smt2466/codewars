# pylint: disable=missing-docstring

"""Stop gninnipS My sdroW!"""

import pytest

from src.stop_gninnips_my_sdrow import spin_words

EXAMPLES = (
    ('sentence', 'expected'),
    [
        ('Welcome', 'emocleW'),
        ('Hey fellow warriors', 'Hey wollef sroirraw'),
        ('This is a test', 'This is a test'),
        ('This is another test', 'This is rehtona test')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(sentence, expected):
    assert spin_words(sentence) == expected
