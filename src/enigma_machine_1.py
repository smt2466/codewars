# pylint: disable=missing-docstring, too-few-public-methods

"""The Enigma Machine - Part 1: The Plugboard
http://www.codewars.com/kata/5523b97ac8f5025c45000900

The plugboard crosswired the 26 letters of the latin alphabet togther, so that
an input into one letter could generate output as another letter. If a wire was
not present, then the input letter was unchanged. Each plugboard came with a
maximum of 10 wires, so at least six letters were not cross-wired.

For example:

If a wire connects A to B, then an A input will generate a B output and a B
input will generate an A output.
If no wire connects to C, then only a C input will generate a C output.
"""


class Plugboard(object):

    def __init__(self, wires=''):
        """
        wires: This is the mapping of pairs of characters
        """
        if len(wires) > 20:
            raise ValueError('Too many wires')

        self.wires = {}

        for wire1, wire2 in (wires[i:i+2] for i in range(0, len(wires), 2)):
            if wire1 in self.wires or wire2 in self.wires:
                raise ValueError('Wire used more than once')
            self.wires[wire1] = wire2
            self.wires[wire2] = wire1

    def process(self, char):
        """
        char: The single character to process
        """
        return self.wires.get(char, char)
