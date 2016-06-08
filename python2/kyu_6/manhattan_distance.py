"""Manhattan Distance
http://www.codewars.com/kata/52998bf8caa22d98b800003a

The distance formula can be used to find the distance between two points.
What if we were trying to walk from point A to point B, but there were
buildings in the way? We would need some other formula..but which?

Manhattan Distance

Manhattan distance is the distance between two points in a grid
(like the grid-like street geography of the New York borough of Manhattan)
calculated by only taking a vertical and/or horizontal path.

Write a function manhattanDistance that accepts two points, pointA and pointB,
and returns the Manhattan Distance between the two points.

pointA and pointB are arrays containing the x and y coordinate in the grid.
You can think of x as the row in the grid, and y as the column.
"""


def manhattan_distance(point1, point2):
    """Calculate manhattan distance between two dots

    Args:
        point1 (list): [x, y] coordinates
        point2 (list): [x, y] coordinates

    Returns:
        int: Manhattan distance

    Examples:
        >>> manhattan_distance([2, 2], [2, 2])
        0
        >>> manhattan_distance([0, 0], [1, 2])
        3
    """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
