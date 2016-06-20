# pylint: disable=missing-docstring

"""Compare Versions"""

import pytest

from python2.kyu_6.compare_versions import compare_versions

EXAMPLES = (
    ('version1', 'version2', 'expected'),
    [
        ('11', '10', True),
        ('11', '11', True),
        ('10.4.6', '10.4', True),
        ('10.4', '10.4.8', False),
        ('10.4', '11', False),
        ('10.4', '10.10', False),
        ('10.4.9', '10.5', False)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(version1, version2, expected):
    assert compare_versions(version1, version2) == expected
