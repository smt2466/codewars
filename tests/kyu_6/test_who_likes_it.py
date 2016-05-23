# pylint: disable=missing-docstring

"""Who likes it?"""

import pytest

from src.kyu_6.who_likes_it import likes

EXAMPLES = (
    ('names', 'expected'),
    [
        (['Peter'], 'Peter likes this'),
        (['Jacob', 'Alex'], 'Jacob and Alex like this'),
        (['Max', 'John', 'Mark'], 'Max, John and Mark like this'),
        (['Alex', 'Jacob', 'Mark', 'Max'], 'Alex, Jacob and 2 others like this')
    ]
)


def test_no_one_likes():
    assert likes([]) == 'no one likes this'


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(names, expected):
    assert likes(names) == expected
