# pylint: disable=missing-docstring

"""Simple Sentences"""

import pytest

from python3.kyu_6.simple_sentance import make_sentences

EXAMPLES = (
    ('parts', 'expected'),
    [
        (['hello', 'world'], 'hello world.'),
        (['hello', ',', 'my', 'dear'], 'hello, my dear.'),
        (['hello', 'world', '.'], 'hello world.'),
        (['hello', 'world', '.', '.', '.'], 'hello world.'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(parts, expected):
    assert make_sentences(parts) == expected
