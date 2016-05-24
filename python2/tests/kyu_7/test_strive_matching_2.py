# coding=utf-8
# pylint: disable=missing-docstring,redefined-outer-name

"""
Genetic Algorithm Series - #2 Mutation tests
"""

import pytest

from python2.src.kyu_7.strive_matching_2 import match


@pytest.fixture
def candidates():
    first = {
        'desires_equity': True,
        'current_location': 'New York',
        'desired_locations': ['San Francisco', 'Los Angeles']
    }
    second = {
        'desires_equity': False,
        'current_location': 'San Francisco',
        'desired_locations': ['Kentucky', 'New Mexico']
    }
    return [first, second]


@pytest.fixture
def job1():
    return {'equity_max': 0, 'locations': ['Los Angeles', 'New York']}


@pytest.fixture
def job2():
    return {'equity_max': 1.2, 'locations': ['New York', 'Kentucky']}


def test_return_correct_result(job1, job2, candidates):
    assert len(match(job1, candidates)) == 0
    assert len(match(job2, candidates)) == 2
