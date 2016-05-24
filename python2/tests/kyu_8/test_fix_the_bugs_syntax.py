# coding=utf-8
# pylint: disable=missing-docstring,invalid-name,singleton-comparison

"""
Test Fix the Bugs (Syntax)
"""

from python2.src.kyu_8.fix_the_bugs_syntax import my_first_kata


def test_returns_correct_result():
    assert my_first_kata(3, 5) == 3 % 5 + 5 % 3
    assert my_first_kata(314, 107) == 107 % 314 + 314 % 107
    assert my_first_kata(1, 32) == 1 % 32 + 32 % 1


def test_negative_arguments():
    assert my_first_kata(-1, -1) == -1 % -1 + -1 % -1


def test_big_arguments():
    assert my_first_kata(19483, 9) == 9 % 19483 + 19483 % 9


def test_first_argument_is_not_number():
    assert my_first_kata("hello", 3) == False


def test_second_argument_is_not_number():
    assert my_first_kata(67, "bye") == False


def test_boolean_arguments():
    assert my_first_kata(True, True) == False


def test_second_argument_is_collection():
    assert my_first_kata("hello", {}) == False


def test_first_argument_is_collection():
    assert my_first_kata([], "pippi") == False


def test_first_argument_is_zero():
    assert my_first_kata(0, 1) == False


def test_second_argument_is_zero():
    assert my_first_kata(1, 0) == False
