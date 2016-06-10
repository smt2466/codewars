"""Generate new kata solution and tests template"""

from collections import namedtuple
import os

from jinja2 import Environment, FileSystemLoader
import requests

STRING_LENGTH = 50

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    loader=FileSystemLoader(os.path.join(PATH, 'templates')))

Kata = namedtuple('Kata', 'name url slug rank description')


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


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

    if response.status_code != 200:
        raise ValueError
    else:
        return response.json()


def limit(line):
    pass


def format_description(description, string_limit=80):
    result = []
    lines = description.split('\n')
    for line in lines:
        result.extend(limit(line))



def process_kata_data(data):
    """Convert raw kata data into manageable namedtuple

    Args:
        data {dict}: Converted to dict json data from response

    Returns:
        namedtuple: Kata(name, url, slug, rank, description)
    """
    name = data['name']
    url = data['url']
    slug = data['slug']
    rank = str(abs(data['rank']['id']))
    description = data['description']
    return Kata(name, url, slug, rank, description)


def create_solution_file(data, python):
    kata = process_kata_data(data)

    filename = kata.slug.replace('-', '_') + '.py'
    full_path = os.path.join('python' + python, 'kyu_' + kata.rank, filename)

    context = {
        'kata': {
            'title': kata.name,
            'python': python,
            'filename': filename,
            'url': kata.url,
            'description': kata.description,
            'rank': kata.rank,
        }
    }

    template = render_template('solution.jinja2', context) + '\n'

    with open(full_path, 'w') as solution:
        solution.write(template)


def create_test_file(data, python):
    pass


def main(slug, python):
    """Create new solution template"""
    access_key = get_env_variable('ACCESS_KEY')

    print('Get kata data...'.ljust(STRING_LENGTH)),
    data = get_kata_data(slug, access_key)
    print('DONE')

    print('Create solution file...'.ljust(STRING_LENGTH))
    create_solution_file(data, python)
    print('DONE')

    print('Create test file...'.ljust(STRING_LENGTH))
    create_test_file(data, python)
    print('DONE')
