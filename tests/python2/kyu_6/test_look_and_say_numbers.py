# coding=utf-8
# pylint: disable=missing-docstring, no-self-use, invalid-name

""""
Look and say numbers
"""

from src.python2.kyu_6.look_and_say_numbers import say, look_and_say


class TestSay(object):

    def test_one_one(self):
        assert say('1') == '11'

    def test_two_one(self):
        assert say('11') == '21'

    def test_one_two__one_one(self):
        assert say('21') == '1211'

    def test_one_one__one_two__two_ones(self):
        assert say('1211') == '111221'

    def test_three_one__two_two__one_one(self):
        assert say('111221') == '312211'

    def test_one_three__one_one__two_two__two_one(self):
        assert say('312211') == '13112221'

    def test_one_one__one_three__two_one__three_two__one_one(self):
        assert say('13112221') == '1113213211'


class TestLookAndSay(object):

    def test_returns_correct_result_start_from_single_digit(self):
        expected = ['11', '21', '1211', '111221', '312211', '13112221',
                    '1113213211', '31131211131221', '13211311123113112211',
                    '11131221133112132113212221']
        assert look_and_say('1', 10) == expected

    def test_returns_correct_result_start_from_multiple_digits(self):
        expected = ['111312', '31131112', '1321133112', '11131221232112',
                    '31131122111213122112', '13211321223112111311222112',
                    '1113122113121122132112311321322112',
                    '311311222113111221221113122112132113121113222112']
        assert look_and_say('132', 8) == expected
