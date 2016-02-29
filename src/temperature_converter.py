# coding=utf-8

"""Temperature converter
http://www.codewars.com/kata/54ce9497975ca65e1a0008c6

Write a function convert_temp(temp, from_scale, to_scale) converting
temperature from one scale to another. Return converted temp value.

Round converted temp value to an integer(!).

Reading: http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature

possible scale inputs:

    "C"  for Celsius
    "F"  for Fahrenheit
    "K"  for Kelvin
    "R"  for Rankine
    "De" for Delisle
    "N"  for Newton
    "Re" for Réaumur
    "Ro" for Rømer

temp is a number, from_scale and to_scale are strings.
"""

FROM = {
    'C': lambda x: x,
    'F': lambda x: (x - 32)*5/9,
    'K': lambda x: x - 273.15,
    'R': lambda x: (x - 491.67)*5/9,
    'De': lambda x: 100 - x*2/3,
    'N': lambda x: x*100/33,
    'Re': lambda x: x*5/4,
    'Ro': lambda x: (x - 7.5)*40/21
}

TO = {
    'C': lambda x: x,
    'F': lambda x: x*9/5 + 32,
    'K': lambda x: x + 273.15,
    'R': lambda x: (x + 273.15)*9/5,
    'De': lambda x: (100 - x)*3/2,
    'N': lambda x: x*33/100,
    'Re': lambda x: x*4/5,
    'Ro': lambda x: x*21/40 + 7.5
}


def convert_temp(temp, from_scale, to_scale):
    """Convert temperature

    Args:
        temp (int, float): Temperature value
        from_scale (str)
        to_scale (str)

    Returns:
        int

    Examples:
        >>> convert_temp(128.25, 'Ro', 'C')
        230
    """
    return int(TO[to_scale](FROM[from_scale](temp)))
