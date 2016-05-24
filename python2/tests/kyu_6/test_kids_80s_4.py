# coding=utf-8
# pylint: disable=invalid-name, missing-docstring

"""80's Kids #4: Legends of the Hidden Temple"""

from python2.src.kyu_6.kids_80s_4 import mark_spot


def test_returns_correct_result_for_5():
    answer = 'X       X\n' \
             '  X   X\n' \
             '    X\n' \
             '  X   X\n' \
             'X       X\n'
    assert mark_spot(5) == answer


def test_long_input():
    answer = 'X                   X\n' \
             '  X               X\n' \
             '    X           X\n' \
             '      X       X\n' \
             '        X   X\n' \
             '          X\n' \
             '        X   X\n' \
             '      X       X\n' \
             '    X           X\n' \
             '  X               X\n' \
             'X                   X\n'
    assert mark_spot(11) == answer


def test_single_x():
    assert mark_spot(1) == 'X\n'


def test_bad_input_list():
    assert mark_spot([]) == '?'


def test_bad_input_string():
    assert mark_spot('treasure') == '?'
