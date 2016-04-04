"""Format a string of names like 'Bart, Lisa & Maggie'.
http://www.codewars.com/kata/53368a47e38700bd8300030d

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas
except for the last two names, which should be separated by an ampersand.
"""


def namelist(names):
    """Convert list of names to string

    Args:
        names (list): List of dicts {'name', '<Name>'}

    Returns:
        str: String 'Name1, Name2 & Name3'

    Examples:
        >>> namelist([{'name': 'Pavel'}, {'name': 'Yury'}])
        'Pavel & Yury'
    """
    if not names:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    else:
        names = [name['name'] for name in names]
        return ', '.join(names[:-1]) + ' & ' + names[-1]
