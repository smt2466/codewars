# pylint: disable=missing-docstring, invalid-name

"""Moves in squared strings (II)"""

import pytest

from python3.src.kyu_6.moves_in_squared_strings_2 import (
    rot, selfie_and_rot, oper
)

ROT_EXAMPLES = (
    ('strng', 'expected'),
    [
        ('fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL',
         'LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif'),
        ('rkKv\ncofM\nzXkh\nflCB',
         'BClf\nhkXz\nMfoc\nvKkr')
    ]
)

SELFIE_AND_ROT_EXAMPLES = (
    ('strng', 'expected'),
    [
        ('xZBV\njsbS\nJcpN\nfVnP',
         'xZBV....\njsbS....\nJcpN....\nfVnP....\n'
         '....PnVf\n....NpcJ\n....Sbsj\n....VBZx'),
        ('uLcq\nJkuL\nYirX\nnwMB',
         'uLcq....\nJkuL....\nYirX....\nnwMB....\n'
         '....BMwn\n....XriY\n....LukJ\n....qcLu')
    ]
)


@pytest.mark.parametrize(*ROT_EXAMPLES)
def test_rot_returns_correct_result(strng, expected):
    assert oper(rot, strng) == expected


@pytest.mark.parametrize(*SELFIE_AND_ROT_EXAMPLES)
def test_selfie_and_rot_returns_correct_result(strng, expected):
    assert oper(selfie_and_rot, strng) == expected
