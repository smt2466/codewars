"""Who likes it?
http://www.codewars.com/kata/5266876b8f4bf2da9b000362

You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items. We want to create
the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input
array, containing the names of people who like an item.
"""


def likes(names):
    """Convert list of names into strings of likes

    Args:
        names (list): List of string names

    Returns:
        str

    Examples:
        >>> likes(['Pavel', 'Yury', 'Sveta'])
        'Pavel, Yury and Sveta like this'
    """
    if not names:
        return 'no one likes this'
    if len(names) == 1:
        first = ''
        second = names[0]
    elif len(names) == 2:
        first = names[0]
        second = names[1]
    elif len(names) == 3:
        first = ', '.join(names[:2])
        second = names[-1]
    else:
        first = ', '.join(names[:2])
        second = '%d others' % (len(names) - 2)
    if first:
        return first + ' and ' + second + ' like this'
    else:
        return second + ' likes this'
    
    # OR...
    
    def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return names[-1] + " likes this"
    elif len(names) == 2 or len(names) == 3:
        return ", ".join(names[:-1]) + " and " + names[-1] + " like this"
    else:
        return ", ".join(names[:2]) + " and " + (str(len(names)-2)) + " others like this"
