"""Human Readable Time
https://www.codewars.com/kata/human-readable-time

Write a function, which takes a non-negative integer (seconds) as input and
returns the time in a human-readable format (`HH:MM:SS`)

* `HH` = hours, padded to 2 digits, range: 00 - 99
* `MM` = minutes, padded to 2 digits, range: 00 - 59
* `SS` = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (`99:59:59`)

You can find some examples in the test fixtures.
"""


def make_readable(seconds):
    """Converts number of seconds into human readable representation"""
    hours = seconds/3600
    seconds -= hours*3600
    minutes = seconds/60
    seconds -= minutes*60
    return '%02d:%02d:%02d' % (hours, minutes, seconds)
