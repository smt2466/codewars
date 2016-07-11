# pylint: disable=missing-docstring

"""Where my anagrams at?"""

import pytest

from python3.kyu_5.where_my_anagrams_at import anagrams


EXAMPLES = (
    ('word', 'words', 'expected'),
    [
        ('abba', ['aabb', 'abcd', 'bbaa', 'dada'], ['aabb', 'bbaa']),
        ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'],
         ['carer', 'racer']),
        ('laser', ['lazing', 'lazy',  'lacer'], []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(word, words, expected):
    assert anagrams(word, words) == expected
