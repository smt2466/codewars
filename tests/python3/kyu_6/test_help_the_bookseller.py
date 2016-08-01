# pylint: disable=missing-docstring

"""Help the bookseller !"""

import pytest

from python3.kyu_6.help_the_bookseller import stock_list

EXAMPLES = (
    ('books', 'categories', 'expected'),
    [
        (['ABAR 200', 'CDXE 500', 'BKWR 250', 'BTSQ 890', 'DRTY 600'],
         ['A', 'B'],
         '(A : 200) - (B : 1140)'),
        (['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600'],
         ['A', 'B', 'C', 'D'],
         '(A : 0) - (B : 1290) - (C : 515) - (D : 600)'),
        ([], ['A', 'B'], '')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(books, categories, expected):
    assert stock_list(books, categories) == expected
