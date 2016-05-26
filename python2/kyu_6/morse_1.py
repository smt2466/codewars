# pylint: disable=invalid-name

"""Decode the Morse code
http://www.codewars.com/kata/54b724efac3d5402db00065e

In this kata you have to write a simple Morse code decoder. While the Morse
code is now mostly superceded by voice and digital data communication channels,
it still has its use in some applications around the world.
"""

# Add MORSE_CODE['  '] = ' '
MORSE_CODE = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
              '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
              '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
              '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
              '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
              '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
              '....': 'H', '.----.': "'", '...-': 'V', '--...': '7',
              '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')',
              '-.-.--': '!', '--.': 'G', '--.-': 'Q', '--..': 'Z', '-..-.': '/',
              '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T',
              '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
              '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8',
              '...--': '3', '': ' '}


def decodeMorse(code):
    """Convert morse code to plain text message

    Args:
        code (str): Morse code

    Returns:
        str: Plain text message

    Examples:
        >>> decodeMorse('...---...')
        'SOS'
    """
    code = code.strip().replace('  ', ' ')
    return ''.join(MORSE_CODE[char] for char in code.split(' '))
