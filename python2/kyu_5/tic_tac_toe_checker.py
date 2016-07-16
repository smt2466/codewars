# pylint: disable=invalid-name

"""Tic-Tac-Toe Checker
https://www.codewars.com/kata/tic-tac-toe-checker

If we were to set up a Tic-Tac-Toe game, we would want to know whether the
board's current state is solved, wouldn't we? Our goal is to create a function
that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0
if a spot is empty, 1 if it is an X, or 2 if it is an O, like so:

```
[[0,0,1],
 [0,1,2],
 [2,1,0]]
```

We want our function to return `-1` if the board is not solved yet,
`1` if X won, `2` if O won, or `0` if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of
Tic-Tac-Toe.
"""

from itertools import chain


def isSolved(board):
    """Check if there is a winner in tic-tac-toe

    Tie         -1
    In progress  0
    X            1
    O            2
    """
    for player in [1, 2]:
        if [player]*3 in chain(
                board,       # Rows
                zip(board),  # Columns
                [            # Diagonals
                    [board[i][i] for i in range(len(board))],
                    [board[len(board) - i - 1][i] for i in range(len(board))]
                ]
        ):
            return player
    return -1 if 0 in chain(*board) else 0
