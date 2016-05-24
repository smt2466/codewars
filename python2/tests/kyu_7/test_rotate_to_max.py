# coding=utf-8
# pylint: disable=missing-docstring

"""
Rotate for a Max tests
"""

from python2.src.kyu_7.rotate_to_max import max_rot


def test_returns_correct_result():
    assert max_rot(38458215) == 85821534
    assert max_rot(195881031) == 988103115
    assert max_rot(896219342) == 962193428
    assert max_rot(69418307) == 94183076
