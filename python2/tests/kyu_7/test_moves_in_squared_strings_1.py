# pylint: disable=missing-docstring, invalid-name

"""Moves in squared strings (I)"""

import pytest

from python2.src.kyu_7.moves_in_squared_strings_1 import vert_mirror, hor_mirror


VERT_MIRROR = (
    ('strng', 'expected'),
    [
        ('hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu',
         'QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw'),
        ('IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx',
         'EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP')
    ]
)


HOR_MIRROR = (
    ('strng', 'expected'),
    [
        ('lVHt\nJVhv\nCSbg\nyeCt', 'yeCt\nCSbg\nJVhv\nlVHt'),
        ('njMK\ndbrZ\nLPKo\ncEYz', 'cEYz\nLPKo\ndbrZ\nnjMK')
    ]
)


@pytest.mark.parametrize(*VERT_MIRROR)
def test_vert_mirror_returns_correct_result(strng, expected):
    assert vert_mirror(strng) == expected


@pytest.mark.parametrize(*HOR_MIRROR)
def test_hor_mirror_returns_correct_result(strng, expected):
    assert hor_mirror(strng) == expected
