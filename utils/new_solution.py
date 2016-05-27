"""Generate new kata solution and tests template"""

import os

import requests


def get_env_variable(var_name):
    """Get environment variable or raise exceptions"""
    try:
        return os.environ[var_name]
    except KeyError:
        raise KeyError('%s environment variable is not set' % var_name)


def get_kata_data(slug, access_key):
    """Get kata data"""
    url = 'https://www.codewars.com/api/v1/code-challenges/%s' % slug
    params = {'access_key': access_key}
    response = requests.get(url, params)
    return response.json()


def main(slug):
    access_key = get_env_variable('ACCESS_KEY')
    kata = get_kata_data(slug, access_key)
