"""Arabian String
http://www.codewars.com/kata/525821ce8e7b0d240b002615

You must create a method that can convert a string from any format into
CamelCase. This must support symbols too.

Don't presume the separators too much or you could be surprised.
"""

import re


def camelize(strng):
    """Convert string to CamelCase

    Args:
        strng (str): String of words

    Returns:
        str: String in CamelCase

    Examples:
        >>> camelize("example name")
        'ExampleName'
        >>> camelize("your-NaMe-here")
        'YourNameHere'
        >>> camelize("testing ABC")
        'TestingAbc'
    """
    return ''.join(word.capitalize() for word in re.split(r'[\W_]', strng))
