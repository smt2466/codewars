# pylint: disable=invalid-name

"""Magic Zeckendorf
http://www.codewars.com/kata/549013f6f71e7786aa0002a8/train/python

Source

This kata is an application of a magic trick. This magic trick is based on a
mathematic algorithm: the Zeckendorf theorem:

    Every positive integer can be expressed uniquely as a sum of distinct
    non-consecutive Fibonacci numbers.

Don't be afraid, you don't need to understand the theorem to solve this kata.

Magic Trick Description

Here is how the magic trick work:

    1. Ask the spectator to choose a number between 0 and 100 (included)
    2. Give a special set of card to the spectator, these cards contains a
       list of numbers. Here is what the cards look like:
       https://blogdemaths.files.wordpress.com/2013/01/cartes-magiques.pdf
    3. Ask the spectator to give you back only the cards where his number is
       written on it.
    4. You can guess the number of your spectator

Magic Trick Explanation

You just need to sum the first number on each card and TADAM. In practice you
could ask numbers much higher (with 10 cards it can go up to 231) but that
would make really long cards.

Objective

We will consider that each presented card has an "index" on it to recognize it.
Those cards are already given to you. Write a class magicZ with 2 functions
gueZZ([indexes of card]) and getMagicZindex(n).

    - gueZZ(indexes) takes an array being the index of each card and return the
      guessed number
    - getMagicZindex(n) takes a number and return the list of indexes for this
      value (the number can be higher than 100)

Example:

I chose number 70:

    gueZZ([1,5,8]) === 70
    getMagicZindex(70) = [1,5,8]

Note

The spectator is always going to try to trick. Be prepared to receive
duplicated cards (ignore the duplicates) or fewer cards than expected
(respond with 0).
"""


class magicZ(object):
    """Zecjendorf magic trick"""

    def __init__(self):
        self.cards = []
        self.cards += [[1, 4, 6, 9, 12, 14, 17, 19, 22, 25, 27, 30, 33, 35,
                        38, 40, 43, 46, 48, 51, 53, 56, 59, 61, 64, 67, 69,
                        72, 74, 77, 80, 82, 85, 88, 90, 93, 95, 98]]
        self.cards += [
            [2, 7, 10, 15, 20, 23, 28, 31, 36, 41, 44, 49, 54, 57, 62, 65, 70,
             75, 78, 83, 86, 91, 96, 99]]
        self.cards += [
            [3, 4, 11, 12, 16, 17, 24, 25, 32, 33, 37, 38, 45, 46, 50, 51, 58,
             59, 66, 67, 71, 72, 79, 80, 87, 88, 92, 93, 100]]
        self.cards += [
            [5, 6, 7, 18, 19, 20, 26, 27, 28, 39, 40, 41, 52, 53, 54, 60, 61,
             62, 73, 74, 75, 81, 82, 83, 94, 95, 96]]
        self.cards += [
            [8, 9, 10, 11, 12, 29, 30, 31, 32, 33, 42, 43, 44, 45, 46, 63, 64,
             65, 66, 67, 84, 85, 86, 87, 88, 97, 98, 99, 100]]
        self.cards += [
            [13, 14, 15, 16, 17, 18, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 68,
             69, 70, 71, 72, 73, 74, 75]]
        self.cards += [
            [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 76, 77, 78, 79,
             80, 81, 82, 83, 84, 85, 86, 87, 88]]
        self.cards += [
            [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
             51, 52, 53, 54]]
        self.cards += [
            [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
             72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
             88]]
        self.cards += [[89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]

    def gueZZ(self, indexes=None):
        """Guesses the number according to card indexes

        Args:
            indexes (list): List of ints of card indexes

        Returns:
            int: Guesses number

        Examples:
            >>> ZZ = magicZ()
            >>> ZZ.gueZZ([1, 3, 5])
            20
        """
        return sum(self.cards[i][0] for i in set(indexes)) if indexes else 0

    def get_magicZ_index(self, num):
        """Returns cards indexes list for card contains num

        Args:
            num (int): Number to search in card

        Returns:
            list: List of ints of card indexes

        Examples:
            >>> ZZ = magicZ()
            >>> ZZ.get_magicZ_index(20)
            [1, 3, 5]
        """
        return [i for i, card in enumerate(self.cards) if num in card]
