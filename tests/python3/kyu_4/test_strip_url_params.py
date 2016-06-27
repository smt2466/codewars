# pylint: disable=missing-docstring

"""Strip Url Params"""

import pytest

from python3.kyu_4.strip_url_params import strip_url_params


EXAMPLES = (
    ('url', 'strip', 'expected'),
    [
        ('www.codewars.com?a=1&b=2&a=2', [], 'www.codewars.com?a=1&b=2'),
        ('www.codewars.com?a=1&b=2&a=2', ['b'], 'www.codewars.com?a=1'),
        ('www.codewars.com', ['b'], 'www.codewars.com'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(url, strip, expected):
    assert strip_url_params(url, strip) == expected
