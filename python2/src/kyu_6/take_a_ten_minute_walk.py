# pylint: disable=invalid-name

"""Take a Ten Minute Walk
http://www.codewars.com/kata/54da539698b8a2ad76000228

You live in the city of Cartesia where all roads are laid out in a perfect
grid. You arrived ten minutes too early to an appointment, so you decided to
take the opportunity to go for a short walk. The city provides its citizens
with a Walk Generating App on their phones -- everytime you press the button
it sends you an array of one-letter strings representing directions to walk
(eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one
city block, so create a function that will return true if the walk the app
gives you will take you exactly ten minutes (you don't want to be early or
late!) and will, of course, return you to your starting point. Return false
otherwise.

Note: you will always receive a valid array containing a random assortment
of direction letters ('n', 's', 'e', or 'w' only). It will never give you an
empty array (that's not a walk, that's standing still!).
"""


def returns_to_start(walk):
    """Check if walk is loopback

    Args:
        walk (list): List of directions 'nsew'

    Returns:
        bool

    Examples:
        >>> returns_to_start(['n', 's', 'e', 'w'])
        True
    """
    return walk.count('n') - walk.count('s') -\
           walk.count('w') + walk.count('e') == 0


def isValidWalk(walk):
    """Check if walk is valid

    - Returns to start
    - Takes 10 minutes (1 minute per block)

    Args:
        walk (list): List of directions 'nsew'

    Returns:
        bool

    Examples:
        >>> isValidWalk(['s', 's', 'n', 'e', 'n', 'n', 's', 'n', 's', 'w'])
        True
    """
    return len(walk) == 10 and returns_to_start(walk)
