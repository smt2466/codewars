# coding=utf-8

"""80's Kids #2: Help ALF Find His Spaceship
http://www.codewars.com/kata/5660aa3d5e011dfd6e000063

Late last night in the Tanner household, ALF was repairing his spaceship so
he might get back to Melmac. Unfortunately for him, he forgot to put on the
parking brake, and the spaceship took off during repair. Now it's hovering
in space.

ALF has the technology to bring the spaceship home if he can lock on to
it's location.

Given a map:

    ..........
    ..........
    ..........
    .......X..
    ..........
    ..........

The map will be given in the form of a string with \n separating new lines.
The bottom left of the map is [0, 0]. X is ALF's spaceship.

In this expample:

If you cannot find the spaceship, the result should be

    "Spaceship lost forever."

Can you help ALF?
"""


def find_spaceship(astromap):
    """Find 'X' coordinates in astromap string

    Args:
        astromap (str): '....\n...X\n....'

    Returns:
        list: 'X' coordinates [3, 2]

    Examples:
        >>> find_spaceship('..X.')
        [2, 0]
        >>> find_spaceship('....')
        'Spaceship lost forever.'
    """
    space = astromap.split('\n')
    pos_y = len(space) - 1
    for line in space:
        try:
            return [line.index('X'), pos_y]
        except ValueError:
            pos_y -= 1
    return 'Spaceship lost forever.'
