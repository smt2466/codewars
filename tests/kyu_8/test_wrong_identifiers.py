# coding=utf-8
# pylint: disable=missing-docstring

"""
What's wrong with these identifiers? tests
"""

import pytest

from src.kyu_8.wrong_identifiers import Person


def test_person_is_defined():
    try:
        Person
    except NameError:
        pytest.fail('Person object is not defined')


def test_person_has_4_properties():
    assert len(Person.keys()) == 4
