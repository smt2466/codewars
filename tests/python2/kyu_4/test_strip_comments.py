# pylint: disable=missing-docstring

"""Strip Comments"""

import pytest

from python2.kyu_4.strip_comments import solution


EXAMPLES = (
    ('text', 'markers', 'expected'),
    [
        ('apples, pears # and bananas\ngrapes\nbananas !apples',
         ['#', '!'], 'apples, pears\ngrapes\nbananas'),
        ('a #b\nc\nd $e f g',
         ['#', '$'], 'a\nc\nd')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, markers, expected):
    assert solution(text, markers) == expected
