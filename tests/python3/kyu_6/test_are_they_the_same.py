# pylint: disable=missing-docstring

"""Are they the "same"?"""

import pytest

from python3.kyu_6.are_they_the_same import comp

EXAMPLES = (
    ('arr1', 'arr2', 'expected'),
    [
        ([121, 144, 19, 161, 19, 144, 19, 11],
         [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144,
          19 * 19],
         True),
        ([1, 2, 3], [1, 4, 9], True),
        ([1, 2, 3], [1, 4, 9, 10], False),
        (None, None, False),
        ([], [], True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arr1, arr2, expected):
    assert comp(arr1, arr2) == expected
