# coding=utf-8
# pylint: disable=missing-docstring,redefined-outer-name

"""
Genetic Algorithm Series - #2 Mutation tests
"""

import pytest

from python2.src.kyu_7.gas_2_mutation import mutate, mutate_gen


@pytest.fixture
def one():
    return '1'*100


@pytest.fixture
def zero():
    return '0'*100


def test_100_mutate_zero(one, zero):
    assert mutate(zero, 1) == one


def test_100_mutate_one(one, zero):
    assert mutate(one, 1) == zero


def test_0_mutate_zero(zero):
    assert mutate(zero, 0) == zero


def test_0_mutate_one(one):
    assert mutate(one, 0) == one


def test_50_mutate_zero(zero):
    assert '0' in mutate(zero, 0.5)


def test_50_mutate_one(one):
    assert '1' in mutate(one, 0.5)


def test_100_mutate_gen_1():
    assert mutate_gen('1', 1) == '0'


def test_100_mutate_gen_0():
    assert mutate_gen('0', 1) == '1'


def test_0_mutate_gen_1():
    assert mutate_gen('1', 0) == '1'


def test_0_mutate_gen_0():
    assert mutate_gen('0', 0) == '0'
