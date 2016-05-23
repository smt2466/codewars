# coding=utf-8

"""String Shortener (shrink)
http://www.codewars.com/kata/557d18803802e873170000a0

Write a function that shortens a string to a given length. Instead of cutting
the string from the end, your function will shorten it from the middle like
shrinking.

For example:

    sentence = "The quick brown fox jumps over the lazy dog"
    res = shorten(sentence, 27)
    res === "The quick br...the lazy dog"

Your function should also accept an optional argument glue to get the parts
together.

    sentence = "The quick brown fox jumps over the lazy dog"
    res = shorten(sentence, 27, '---')
    res === "The quick br---the lazy dog"

Rules are simple:

    - Result should never be longer or shorter than the given length
    - Only exception to above rule is when string is already shorter than
      given length, in that case string should be returned untouched.
    - If no glue is sent ... should be used by default
    - If glue cannot go exactly in the middle, second part should be longer
    - If glue cannot fit in the shortened string, string should be shortened
      without shrinking.
        + meaning; shorten('hello world', 5, '....') should return hello
          because 4 char glue cannot fit in the shortened string.
        + glue must have at least 1 char on both ends. example minimum h...d,
          results ....d or h.... are not excepted.
    - You can assume you'll always receive string as the sentence and the
      glue. And integer number for the length.
    - Think about other possible edge cases, there are some surprises.
"""


def shorten(string, length, glue='...'):
    """Shorten string in the middle

    Args:
        string (str): String to be shorten
        length (int): Result string length
        glue (str): Template to put inside the string

    Returns:
        str

    Examples:
        >>> shorten('Go ye into the streets and by ways of Jerusalem', 20)
        'Go ye in...Jerusalem'
    """
    if len(string) < length or \
       len(string) < len(glue) + 2 or \
       len(glue) + 2 > length:
        return string[:length]
    else:
        start = (length - len(glue))/2
        end = -start if len(glue) % 2 == length % 2 else -start - 1
        return string[:start] + glue + string[end:]
