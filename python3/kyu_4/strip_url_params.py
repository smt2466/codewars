"""Strip Url Params
https://www.codewars.com/kata/strip-url-params

#####Complete the method so that it does the following:

- Removes any duplicate query string parameters from the url
- Removes any query string parameters specified within the 2nd argument
  (optional array)
"""

from urllib import parse


def strip_url_params(url, strip=()):
    """Remove duplicate parameters and parameters in strip from the url

    Args:
        url (str): URL to parse
        strip (iterable): List of parameters to remove

    Returns:
        str: Fixed url
    """
    scheme, netloc, path, query_string, fragment = parse.urlsplit(url)
    query_params = parse.parse_qsl(query_string)

    seen = []
    new_query_params = []
    for key, value in query_params:
        if key not in strip and key not in seen:
            seen.append(key)
            new_query_params.append((key, value[0]))
    new_query_string = parse.urlencode(new_query_params, doseq=True)

    return parse.urlunsplit((scheme, netloc, path, new_query_string, fragment))
