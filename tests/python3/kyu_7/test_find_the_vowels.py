# pylint: disable=missing-docstring

"""Find the vowels"""

import pytest

from python3.kyu_7.find_the_vowels import vowel_indices

EXAMPLES = (
    ('word', 'expected'),
    [
        ('Mmmm', []),
        ('Super', [2, 4]),
        ('Apple', [1, 5]),
        ('YoMama', [1, 2, 4, 6])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(word, expected):
    assert vowel_indices(word) == expected
