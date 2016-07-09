# pylint: disable=missing-docstring

"""ROT13"""

import pytest

from python3.kyu_5.rot13 import rot13


EXAMPLES = (
    ('message', 'expected'),
    [
        ('EBG13 rknzcyr.', 'ROT13 example.'),
        ('This is my first ROT13 excercise!',
         'Guvf vf zl svefg EBG13 rkprepvfr!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(message, expected):
    assert rot13(message) == expected
