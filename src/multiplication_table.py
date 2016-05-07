"""Multiplication Tables
http://www.codewars.com/kata/5432fd1c913a65b28f000342

Create a function that accepts dimensions, of Rows x Columns, as parameters
in order to create a multiplication table sized according to the given
dimensions. **The return value of the function must be an array, and the
numbers must be Fixnums, NOT strings.
"""


def multiplication_table(rows, cols):
    """Create multiplication table

    Args:
        rows (int): Number of rows
        cols (int): Number of columns

    Returns:
        list: Multiplication table (2D matrix)

    Examples:
        >>> multiplication_table(2, 3)
        [[1, 2, 3], [2, 4, 6]]
    """
    return [[i*j for i in range(1, cols + 1)] for j in range(1, rows + 1)]
