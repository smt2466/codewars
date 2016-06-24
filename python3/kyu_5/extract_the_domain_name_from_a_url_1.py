"""Extract the domain name from a URL
https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1

Write a function that when given a URL as a string, parses out just the domain
name and returns it as a string.
"""

import re

DOMAIN_PATTERN = re.compile(r'(?:https?://)?(?:www.)?([\w-]*)')


def domain_name(url):
    """Extract domain name from the url

    Args:
        url (str): Url address

    Returns:
        str: Domain name or empty string

    Examples:
        >>> domain_name('www.ya.ru')
        'ya'
        >>> domain_name('http://www.ya.ru')
        'ya'
    """
    match = re.match(DOMAIN_PATTERN, url)
    if match:
        return match.groups()[0]
    else:
        return ''
