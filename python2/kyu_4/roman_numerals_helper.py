"""Roman Numerals Helper
https://www.codewars.com/kata/roman-numerals-helper

Create a RomanNumerals helper that can convert a roman numeral to and from an
integer value.  The class should follow the API demonstrated in the examples
below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero. In Roman
numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is
written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in
descending order: MDCLXVI.
"""

FROM_ROMAN = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


TO_ROMAN = [
    (1000, 'M'),
    (500, 'D'),
    (100, 'C'),
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
]


class RomanNumerals(object):
    """Roman-Numeric and Numeric-Roman converter"""

    @staticmethod
    def to_roman(number):
        """Converts numeric to roman

        Args:
            number (int): Numeric

        Returns:
            str: Roman

        Examples:
            >>> RomanNumerals.to_roman(8)
            'VIII'
        """
        result = ''
        for i, (numeric, roman) in enumerate(TO_ROMAN):
            current = number//numeric
            if current:
                if str(number)[0] == '4':
                    result += roman + TO_ROMAN[i - 1][1]
                    number -= numeric + TO_ROMAN[i - 1][0]
                elif str(number)[0] == '9':
                    result += TO_ROMAN[i + 1][1] + TO_ROMAN[i - 1][1]
                    number -= TO_ROMAN[i + 1][0] + TO_ROMAN[i - 1][0]
                else:
                    result += roman*current
                    number -= numeric*current
        return result

    @staticmethod
    def from_roman(number):
        """Converts roman to numeric

        Args:
            number (str): Roman

        Returns:
            int: Numeric

        Examples:
            >>> RomanNumerals.from_roman('VIII')
            8
        """
        result = 0
        i = 0
        while i < len(number):
            current = FROM_ROMAN[number[i]]
            try:
                following = FROM_ROMAN[number[i+1]]

                if current >= following:
                    result += current
                else:
                    result += following - current
                    i += 1
            except IndexError:
                result += current
            finally:
                i += 1
        return result
