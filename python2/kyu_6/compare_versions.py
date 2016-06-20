"""Compare Versions
https://www.codewars.com/kata/53b138b3b987275b46000115

Karan's company makes software that provides different features based on the
version of operating system of the user.

For finding which version is more recent, Karan uses the following method:

While this function worked for OS versions 10.6, 10.7, 10.8 and 10.9, the
Operating system company just released OS version 10.10.

Karan's function fails for the new version:

compareVersions ("10.9", "10.10");       // returns true, while it should
return false
Karan now wants to spend some time to right a more robust version comparison
function that works for any future version/sub-version updates.

Help Karan write this function. Here are a few sample cases:

It can be assumed that version strings are non empty and only contain numeric
literals and the character '.'
"""

from itertools import izip_longest


def compare_versions(version1, version2):
    """Is first version equal or greater than second

    Args:
        version1 (str): ex. '1.2.3'
        version2 (str): ex. '1.2.3'

    Returns:
        bool: True if first version if greater or equal to the second

    Examples:
        >>> compare_versions('1.2', '1.3')
        False
        >>> compare_versions('1.2', '1.1')
        True
    """
    version1 = version1.split('.')
    version2 = version2.split('.')

    for sub_version1, sub_version2 in izip_longest(version1, version2):
        if not sub_version1:
            return False
        if not sub_version2:
            return True

        if int(sub_version1) < int(sub_version2):
            return False

    return True
