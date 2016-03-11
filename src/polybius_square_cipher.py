"""Polybius square cipher - encode
http://www.codewars.com/kata/542a823c909c97da4500055e

Implement the Polybius square cipher.

Replace every letter with a two digit number. The first digit is the row
number, and the second digit is the column number of following square.
Letters 'I' and 'J' are both 24 in this cipher:

        1	2	3	4	5
    1	A	B	C	D	E
    2	F	G	H	I/J	K
    3	L	M	N	O	P
    4	Q	R	S	T	U
    5	V	W	X	Y	Z

Input will be valid (only spaces and uppercase letters from A to Z), so no
need to validate them.
"""

from string import ascii_uppercase

CHARS = ascii_uppercase.replace('J', '')


def polybius(text):
    """Polybius cipher implementation

    Args:
        text (str): Text to encode

    Returns:
        str: Cipher text

    Examples:
        >>> polybius('A')
        '11'
        >>> polybius('POLYBIUS SQUARE CIPHER')
        '3534315412244543 434145114215 132435231542'
        >>> polybius('IJ')
        '2424'
        >>> polybius('CODEWARS')
        '1334141552114243'
    """
    cipher_text = ''
    for char in text:
        try:
            row = str(CHARS.index(char)/5 + 1)
            col = str((CHARS.index(char) % 5) + 1)
            cipher_text += row + col
        except ValueError:
            if char == 'J':
                cipher_text += '24'
            else:
                cipher_text += ' '
    return cipher_text
