# pylint: disable=no-self-use, missing-docstring, invalid-name

""""Dragon's Curve"""

from src.kyu_6.dragons_curve import change, Dragon


class ChangeTest(object):

    def test_a(self):
        assert change('a') == 'aRbFR'

    def test_b(self):
        assert change('b') == 'LFaLb'

    def test_x(self):
        assert change('x') == 'x'


class DragonTest(object):

    def test_zero_iterations(self):
        assert Dragon(0) == 'F'

    def test_one_iteration(self):
        assert Dragon(1) == 'FRFR'

    def test_two_iterations(self):
        assert Dragon(2) == 'FRFRRLFLFR'

    def test_can_handle_error_values(self):
        assert Dragon('a') == ''

    def test_can_handle_negative_numbers(self):
        assert Dragon(-1) == ''
