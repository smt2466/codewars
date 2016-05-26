# pylint: disable=missing-docstring, invalid-name

"""Dubstep"""

from python2.kyu_6.dubstep import song_decoder


def test_replace_wub_by_one_space():
    assert song_decoder('AWUBBWUBC') == 'A B C'


def test_replace_multiple_wub_by_one_space():
    assert song_decoder('AWUBWUBWUBBWUBWUBWUBC') == 'A B C'


def test_heading_or_trailing_space_should_be_removed():
    assert song_decoder('WUBAWUBBWUBCWUB') == 'A B C'
