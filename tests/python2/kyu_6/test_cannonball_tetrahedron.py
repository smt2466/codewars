# pylint: disable=invalid-name, missing-docstring

"""A tetrahedron of cannonballs"""

import pytest

from python2.kyu_6.cannonball_tetrahedron import (
    triangular,
    tetrahedron
)

TRIANGULAR = (
    ('num', 'expected'),
    [
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
        (6, 21),
        (7, 28),
        (8, 36),
        (9, 45),
        (10, 55),
        (11, 66),
        (12, 78),
        (13, 91),
        (14, 105),
        (15, 120),
        (20, 210),
    ]
)

TETRAHEDRON = (
    ('size', 'expected'),
    [
        (1, 1),
        (2, 4),
        (3, 10),
        (11, 286),
        (17, 969),
        (47, 18424),
        (200, 1353400),
        (1357, 417395559),
        (797651, 84584176417339026),
        (200, 1353400),
        (116332, 262396195030284),
        (9706843691, 152434355365411589198991264366),
        (40075634145, 10727288466058648073779549751665),
    ]
)


@pytest.mark.parametrize(*TRIANGULAR)
def test_triangular_returns_correct_result(num, expected):
    assert triangular(num) == expected


@pytest.mark.parametrize(*TETRAHEDRON)
def test_tetrahedron_returns_correct_result(size, expected):
    assert tetrahedron(size) == expected
