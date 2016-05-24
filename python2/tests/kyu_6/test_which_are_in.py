# pylint: disable=missing-docstring, redefined-outer-name

"""Which are in?"""

import pytest

from python2.src.kyu_6.which_are_in import in_array


@pytest.fixture()
def array2():
    return ['lively', 'alive', 'harp', 'sharp', 'armstrong']


def test_all_in(array2):
    array1 = ['live', 'arp', 'strong']
    assert in_array(array1, array2) == ['arp', 'live', 'strong']


def test_nothing_in(array2):
    array1 = ['tarp', 'mice', 'bull']
    assert in_array(array1, array2) == []


def test_ignore_duplicates():
    assert in_array(['a', 'a'], ['a', 'a']) == ['a']
