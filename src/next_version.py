# coding=utf-8

"""Next Version
http://www.codewars.com/kata/56c0ca8c6d88fdb61b000f06

You're fed up about changing the version of your software manually. Instead,
you will create a little script that will make it for you.

Create a function nextVersion, that will take a string in parameter, and will
return a string containing the next version number.

For example:

    nextVersion("1.2.3") === "1.2.4";
    nextVersion("0.9.9") === "1.0.0.";
    nextVersion("1") === "2";
    nextVersion("1.2.3.4.5.6.7.8") === "1.2.3.4.5.6.7.9";
    nextVersion("9.9") === "10.0";

Rules

    All numbers, except the first one, must not be greater than 10:
    if there are, you have to set them to 0 and increment the next number
    in sequence.

    You can assume all tests inputs to be valid.
"""


def next_version(version):
    """Increment version number by one

    Args:
        version (str): '1.0.0'

    Returns:
        str: New version '1.0.1'

    Examples:
        >>> next_version('1.0.0')
        '1.0.1'
    """
    dots = version.count('.')

    new = str(int(version.replace('.', '')) + 1)  # Increment version
    new = '.'.join(new)
    new = new.replace('.', '', new.count('.') - dots)  # Remove extra dots

    return new
