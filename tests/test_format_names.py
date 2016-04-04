# pylint: disable=missing-docstring

"""Format a string of names like 'Bart, Lisa & Maggie'."""

import pytest

from src.format_names import namelist


EXAMPLES = (
    ('names', 'expected'),
    [
        ([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},
          {'name': 'Homer'}, {'name': 'Marge'}],
         'Bart, Lisa, Maggie, Homer & Marge'),
        ([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}],
         'Bart, Lisa & Maggie'),
        ([{'name': 'Bart'}, {'name': 'Lisa'}],
         'Bart & Lisa')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(names, expected):
    assert namelist(names) == expected


def test_single_name():
    assert namelist([{'name': 'Bart'}]) == 'Bart'


def test_empty_list():
    assert namelist([]) == ''
