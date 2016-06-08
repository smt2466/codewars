# pylint: disable=invalid-name

"""Good vs Evil
http://www.codewars.com/kata/52761ee4cffbc69732000738

Middle Earth is about to go to war. The forces of good will have many battles
with the forces of evil. Different races will certainly be involved. Each race
has a certain 'worth' when battling against others. On the side of good we have
the following races, with their associated worth:

    Hobbits - 1
    Men - 2
    Elves - 3
    Dwarves - 3
    Eagles - 4
    Wizards - 10

On the side of evil we have:

    Orcs - 1
    Men - 2
    Wargs - 2
    Goblins - 2
    Uruk Hai - 3
    Trolls - 5
    Wizards - 10

Although weather, location, supplies and valor play a part in any battle, if
you add up the worth of the side of good and compare it with the worth of the
side of evil, the side with the larger worth will tend to win.

Thus, given the count of each of the races on the side of good, followed by the
count of each of the races on the side of evil, determine which side wins.

Input:

The function will be given two parameters. Each parameter will be a string
separated by a single space. Each string will contain the count of each race on
the side of good and evil.

The first parameter will contain the count of each race on the side of good in
the following order:

    Hobbits, Men, Elves, Dwarves, Eagles, Wizards.

The second parameter will contain the count of each race on the side of evil in
the following order:

    Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.

All values are non-negative integers. The resulting sum of the worth for each
side will not exceed the limit of a 32-bit integer.

Output:

Return ""Battle Result: Good triumphs over Evil" if good wins, "Battle Result:
Evil eradicates all trace of Good" if evil wins, or "Battle Result: No victor
on this battle field" if it ends in a tie.
"""

GOOD_WINS = 'Battle Result: Good triumphs over Evil'
EVIL_WINS = 'Battle Result: Evil eradicates all trace of Good'
TIE = 'Battle Result: No victor on this battle field'

GOOD_STATS = (1, 2, 3, 3, 4, 10)
EVIL_STATS = (1, 2, 2, 2, 3, 5, 10)


def goodVsEvil(good, evil):
    """Compare powers of good and evil armies

    Args:
        good (str): Count of each good race separated by space
        evil (str): Count of each evil race separated by space

    Returns:
        str: Battle result

    Examples:
        >>> goodVsEvil('1 1 1 1 1 5', '10 5 1 1 1 1 1')
        'Battle Result: Good triumphs over Evil'
    """
    good = [int(num) for num in good.split(' ')]
    evil = [int(num) for num in evil.split(' ')]
    good_power = sum(num*power for num, power in zip(good, GOOD_STATS))
    evil_power = sum(num*power for num, power in zip(evil, EVIL_STATS))

    if good_power > evil_power:
        return GOOD_WINS
    elif evil_power > good_power:
        return EVIL_WINS
    else:
        return TIE
