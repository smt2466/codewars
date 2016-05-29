"""Remove anchor from URL
http://www.codewars.com/kata/51f2b4448cadf20ed0000386

Complete the function/method so that it returns the url with anything after
the anchor (#) removed.
"""


def remove_url_anchor(url):
    """Remove anchor from url and anything after it

    Args:
        url (str): Url for parsing

    Returns:
        str: url without anchor part

    Examples:
        >>> remove_url_anchor('www.example.com#hello')
        'www.example.com'
    """
    anchor = url.find('#')
    return url[:anchor] if anchor > 0 else url
