"""Moves in squared strings (II)
http://www.codewars.com/kata/56dbe7f113c2f63570000b86

You are given a string of n lines, each substring being n characters long:
For example:

    s = "abcd\nefgh\nijkl\nmnop"

We will study some transformations of this square of strings.

    - Clock rotation 180 degrees: rot

        rot(s) => "ponm\nlkji\nhgfe\ndcba"

    - selfie_and_rot(s) (or selfieAndRot or selfie-and-rot) It is initial
      string + string obtained by clock rotation 180 degrees with dots
      interspersed in order (hopefully) to better show the rotation when
      printed.

        s = "abcd\nefgh\nijkl\nmnop" -->
        "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe"
        "\n....dcba"

    or printed:

        |rotation        |selfie_and_rot
        |abcd --> ponm   |abcd --> abcd....
        |efgh     lkji   |efgh     efgh....
        |ijkl     hgfe   |ijkl     ijkl....
        |mnop     dcba   |mnop     mnop....
                                   ....ponm
                                   ....lkji
                                   ....hgfe
                                   ....dcba

Task:

    - Write these two functions rotand selfie_and_rot

and

    - high-order function oper(fct, s) where
        - fct is the function of one variable f to apply to the string s
          (fct will be one of rot, selfie_and_rot)

Notes:

    - The form of the parameter fct in oper changes according to the language.
      You can see each form according to the language in "Your test cases".
    - It could be easier to take these katas from number (I) to number (IV)
"""


def rot(strng):
    """Clock rotation 180 degrees

    Args:
        strng (str): N lines of N length separated by '\n'

    Returns:
        str

    Examples:
        >>> s = 'abcd\\nefgh\\nijkl\\nmnop'
        >>> rot(s)
        'ponm\\nlkji\\nhgfe\\ndcba'
    """
    lines = strng.split('\n')[::-1]
    return '\n'.join(line[::-1] for line in lines)


def selfie_and_rot(strng):
    """Clock rotation 180 degrees and initial lines

    Args:
        strng (str): N lines of N length separated by '\n'

    Returns:
        str

    Examples:
        >>> s = 'ab\\nef'
        >>> selfie_and_rot(s)
        'ab..\\nef..\\n..fe\\n..ba'
    """
    lines = strng.split('\n')
    rot_lines = rot(strng).split('\n')

    lines = [line + '.'*len(lines) for line in lines]
    rot_lines = ['.'*len(lines) + line for line in rot_lines]
    return '\n'.join(lines + rot_lines)


def oper(fct, strng):
    """Apply fct to strng

    Args:
        fct (function): Function to apply
        strng (str): N lines of N length separated by '\n'

    Returns:
        str
    """
    return fct(strng)
