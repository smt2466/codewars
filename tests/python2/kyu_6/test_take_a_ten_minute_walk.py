# pylint: disable=missing-docstring, singleton-comparison, no-self-use

"""Take a Ten Minute Walk"""

from python2.kyu_6.take_a_ten_minute_walk import returns_to_start, isValidWalk


class ReturnsToStartTest(object):

    def test_returns_to_start(self):
        walk = ['n', 'e', 'w', 's']
        assert returns_to_start(walk) == True

    def test_not_returns_to_start(self):
        walk = ['n', 's', 's', 'e', 'n', 'w', 'e', 'e', 'w', 's']
        assert returns_to_start(walk) == False


class IsValidWalkTest(object):

    def test_too_short(self):
        walk = ['n', 'e', 'w', 's']
        assert isValidWalk(walk) == False

    def test_not_loopback(self):
        walk = ['n', 's', 's', 'e', 'n', 'w', 'e', 'e', 'w', 's']
        assert isValidWalk(walk) == False
