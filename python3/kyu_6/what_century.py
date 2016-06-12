# pylint: disable=invalid-name

"""What century is it?
https://www.codewars.com/kata/52fb87703c1351ebd200081f

Return the inputted numerical year in century format. For example 2014, would
return 21st.

The input will always be a 4 digit string. So there is no need for year string
validation
"""

import math


def whatCentury(year):
    """Compute year century

    Args:
        year (str): Year (ex. 1988)

    Returns:
        str: Century (ex. 20th)

    Examples:
        >>> whatCentury('1988')
        '20th'
    """
    century = math.ceil(int(year)/100)
    if 10 < century < 21:
        end = 'th'
    elif century % 10 == 1:
        end = 'st'
    elif century % 10 == 2:
        end = 'nd'
    elif century % 10 == 3:
        end = 'rd'
    else:
        end = 'th'
    return str(century) + end
