"""ROT13
https://www.codewars.com/kata/rot13

How can you tell an extrovert from an introvert at NSA? Va gur ryringbef,
gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can
decipher it?

According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is
frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces,
punctuation, numbers etc.
"""

from string import ascii_lowercase as low
from string import ascii_uppercase as upr


def rot13(message):
    """Decode ROT13 message"""
    table = str.maketrans(low + upr, low[13:] + low[:13] + upr[13:] + upr[:13])
    return message.translate(table)
