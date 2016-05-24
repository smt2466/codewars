# coding=utf-8
# pylint: disable=invalid-name

""""Angle Between Clock Hands
http://www.codewars.com/kata/angle-between-clock-hands

Given a Date, return the angle between the two hands of a 12-hour analog clock
in radians.

For example, at 3:00 the angle is π/2 (90 degrees).

Return the smaller of the angles ( <= π ).

Return π if the hands are opposite.

Note: The hour hand does not "snap" to the tick mark - e.g. at 6:30 the angle
is not 0 because the hour hand is at 6.5, not 6.0.

There is no "seconds" hand, so the minutes hand snaps to the minute.
"""

import math


def handAngle(hours, minutes):
    """Calculate angle between clock hands

    Args:
        hours (int)
        minutes (int)

    Returns:
        float: Angle in radians

    Examples:
        >>> handAngle(3, 0)
        1.5707963267948966
    """
    angle = math.pi*abs(hours % 12 - 11*minutes/60.0)/6
    return angle if angle <= math.pi else 2*math.pi - angle
