"""Bracket Duplicates
https://www.codewars.com/kata/bracket-duplicates

Create a program that will take in a string as input and, if there are
duplicates of more than two alphabetical characters in the string, returns
the string with all the extra characters in a bracket.

For example, the input "aaaabbcdefffffffg" should return
"aa[aa]bbcdeff[fffff]g"

Please also ensure that the input is a string, and return "Please enter a valid
string" if it is not.
"""


def string_parse(string):
    """Enclose duplicated letters after second into brackets"""
    result = ''
    count = 0
    brackets = False

    for i, letter in enumerate(string):
        if i == 0:
            count += 1
            result += letter
        elif letter == string[i-1]:
            count += 1
            if count == 3:
                result += '[' + letter
                brackets = True
            else:
                result += letter
        else:
            if count > 2:
                result += ']'
                brackets = False
            result += letter
            count = 1
    if brackets:
        result += ']'
    return result
