# pylint: disable=missing-docstring

"""Codewar's style ranking system"""

import pytest

from python3.kyu_4.codewars_style_ranking_system import User


@pytest.fixture
def user():
    return User()


def test_starts_with_rank_8(user):
    assert user.rank == -8


def test_starts_with_0_progress(user):
    assert user.progress == 0


def test_complete_1_level_high_activity(user):
    user.inc_progress(-7)
    assert user.progress == 10


def test_rank_up(user):
    user.inc_progress(-7)
    user.inc_progress(-5)
    assert user.progress == 0
    assert user.rank == -7


def test_multiple_rank_ups(user):
    user.inc_progress(1)
    assert user.rank == -2


def test_can_not_go_beyond_8_rank(user):
    user._rank = 15
    user.inc_progress(1)
    assert user.progress == 0


def test_1(user):
    user.inc_progress(8)
    assert user.progress == 0


@pytest.mark.parametrize('rank', [-9, 9, 0])
def test_invalid_ranks(user, rank):
    with pytest.raises(ValueError):
        user.inc_progress(rank)
