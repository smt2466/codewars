"""Pretty date
https://www.codewars.com/kata/53988ee02c2414dbad000baa

Write a helper function that takes in a Time object and converts it to a more
human-readable format. You need only go up to '_ weeks ago'.

    to_pretty(0) => "just now"

    to_pretty(40000) => "11 hours ago"

Specifics

    - The output will be an amount of time, t, included in one of the following
      phrases: "just now", "[t] seconds ago", "[t] minutes ago", "[t] hours
      ago", "[t] days ago", "[t] weeks ago".
    - You will have to handle the singular cases. That is, when t = 1,
      the phrasing will be one of "a second ago", "a minute ago", "an hour
      ago", "a day ago", "a week ago".
    - The amount of time is always rounded down to the nearest integer.
      For example, if the amount of time is actually 11.73 hours ago,
      the return value will be "11 hours ago".
    - Only times in the past will be given, with the range "just now" to
      "52 weeks ago"
"""


TIME_UNITS = [
    ('week', 7*24*60*60),
    ('day', 24*60*60),
    ('hour', 60*60),
    ('minute', 60),
    ('second', 1),
]


def plural(number, unit):
    """Creates message from number of units and unit type

    Args:
        number (int): Number of units
        unit (str): Time unit type (week, hour, etc.)

    Returns:
        str: Formatted message

    Examples:
        >>> plural(2, 'hour')
        '2 hours ago'
        >>> plural(1, 'hour')
        'an hour ago'
    """
    if number != 1:
        return '%d %ss ago' % (number, unit)
    else:
        article = 'an' if unit == 'hour' else 'a'
        return '%s %s ago' % (article, unit)


def to_pretty(seconds):
    """Plural seconds time representation

    Args:
        seconds (int): Number of seconds

    Returns:
        str: Formatted message

    Examples:
        >>> to_pretty(60)
        'a minute ago'
        >>> to_pretty(7200)
        '2 hours ago'
    """
    seconds = int(seconds)
    if not seconds:
        return 'just now'
    for unit, seconds_per_unit in TIME_UNITS:
        units = seconds/seconds_per_unit
        if units:
            return plural(units, unit)
