# pylint: disable=missing-docstring

"""Build a pile of Cubes"""

from python2.src.kyu_6.pile_of_cubes import find_nb


def test_returns_correct_result():
    assert find_nb(4183059834009) == 2022
    assert find_nb(135440716410000) == 4824
    assert find_nb(40539911473216) == 3568
    assert find_nb(26825883955641) == 3218


def test_cannot_build_a_pile():
    assert find_nb(24723578342962) == -1
    assert find_nb(10252519345963644753026) == -1
