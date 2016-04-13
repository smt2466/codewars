# pylint: disable=missing-docstring

"""Get All Possible Anagrams from a Hash"""

import pytest

from src.get_anagrams import get_words

EXAMPLES = (
    ('hash_of_letters', 'expected'),
    [
        ({1: ['a', 'b', 'c']}, ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),
        ({2: ['a'], 1: ['b', 'c']}, ['aabc', 'aacb', 'abac', 'abca', 'acab',
                                     'acba', 'baac', 'baca', 'bcaa', 'caab',
                                     'caba', 'cbaa'])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(hash_of_letters, expected):
    assert get_words(hash_of_letters) == expected
