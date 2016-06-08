# pylint: disable=missing-docstring

"""Remove anchor from URL"""

import pytest

from python3.kyu_6.remove_anchor import remove_url_anchor

EXAMPLES = (
    ('url', 'expected'),
    [
        ('www.codewars.com#about', 'www.codewars.com'),
        ('www.codewars.com?page=1', 'www.codewars.com?page=1'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(url, expected):
    assert remove_url_anchor(url) == expected
