# pylint: disable=missing-docstring

"""Extract the domain name from a URL"""

import pytest

from python3.kyu_5.extract_the_domain_name_from_a_url_1 import domain_name


EXAMPLES = (
    ('url', 'expected'),
    [
        ('http://github.com/carbonfive/raygun', 'github'),
        ('http://www.zombie-bites.com', 'zombie-bites'),
        ('https://www.cnet.com', 'cnet'),
        ('www.xakep.ru', 'xakep'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(url, expected):
    assert domain_name(url) == expected
