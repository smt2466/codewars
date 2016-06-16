# pylint: disable=invalid-name

"""Keyword Cipher Helper
https://www.codewars.com/kata/535c1c80cdbf5011e600030f

A keyword cipher is a monoalphabetic cipher which uses a "keyword" to provide
encryption. It is somewhat similar to a Caesar cipher.

In a keyword cipher, repeats of letters in the keyword are removed and the
alphabet is reordered such that the letters in the keyword appear first,
followed by the rest of the letters in the alphabet in their otherwise usual
order.

E.g. for an uppercase latin alphabet with keyword of "KEYWORD":

    A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z

becomes:

    K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z

such that:

    cipher.encode('ABCHIJ') == 'KEYABC'
    cipher.decode('KEYABC') == 'ABCHIJ'

All letters in the keyword will also be in the alphabet. For the purpose of
this kata, only the first occurence of a letter in a keyword should be used.
Any characters not provided in the alphabet should be left in situ when
encoding or decoding.
"""


class keyword_cipher(object):
    """Keyword Cipher"""

    def __init__(self, abc, keyword):
        """
        Args:
            abc (str): Alphabet as base for encoding
            keyword (str): Keyword for cipher
        """
        keyword = ''.join(sorted(set(keyword), key=keyword.index))
        cipher = keyword + ''.join(char for char in abc if char not in keyword)
        self.encode_table = str.maketrans(abc, cipher)
        self.decode_table = str.maketrans(cipher, abc)

    def encode(self, text):
        """Encodes text with Keyword Cipher"""
        return text.translate(self.encode_table)

    def decode(self, text):
        """Decides text with Keyword Cipher"""
        return text.translate(self.decode_table)
