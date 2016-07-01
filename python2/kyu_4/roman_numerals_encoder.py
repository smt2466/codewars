"""Roman Numerals Encoder
https://www.codewars.com/kata/roman-numerals-encoder

Create a function taking a positive integer as its parameter and returning a
string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero. In Roman
numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is
written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in
descending order: MDCLXVI.

Help:
```
Symbol	Value
I	      1
V	      5
X	      10
L	      50
C	      100
D	      500
M	      1,000
```

Remember that there can't be more than 3 identical symbols in a row.
"""

ROMAN_MAP = [
    (1000, 'M'),
    (500, 'D'),
    (100, 'C'),
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
]


def solution(num):
    """Convert numeric integer into roman number

    Args:
        num (int): Numeric integer

    Returns:
        str: Roman number

    Examples:
        >>> solution(14)
        'XIV'
    """
    result = ''
    for i, (numeric, roman) in enumerate(ROMAN_MAP):
        current = num//numeric
        if current:
            if str(num)[0] == '4':
                result += roman + ROMAN_MAP[i-1][1]
                num -= numeric + ROMAN_MAP[i-1][0]
            elif str(num)[0] == '9':
                result += ROMAN_MAP[i+1][1] + ROMAN_MAP[i-1][1]
                num -= ROMAN_MAP[i+1][0] + ROMAN_MAP[i-1][0]
            else:
                result += roman*current
                num -= numeric*current
    return result
