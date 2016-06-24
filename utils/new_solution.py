"""Generate new kata solution and tests template"""

from collections import namedtuple
import os
import sys

from jinja2 import Environment, FileSystemLoader
import requests

STRING_LENGTH = 30

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


def create_file(data, python, file_type):
    if file_type == 'solution':
        filename = data.slug.replace('-', '_') + '.py'
        directory = os.path.join(python, 'kyu_' + data.rank)
        full_path = os.path.join(directory, filename)
    elif file_type == 'test':
        filename = 'test_' + data.slug.replace('-', '_') + '.py'
        directory = os.path.join('tests', python, 'kyu_' + data.rank)
        full_path = os.path.join(directory, filename)
    else:
        raise ValueError('Unknown file type')

    context = {
        'kata': {
            'title': data.name,
            'python': python,
            'filename': data.slug.replace('-', '_'),
            'url': data.url,
            'description': data.description,
            'rank': data.rank,
        }
    }

    template = render_template('%s.jinja2' % file_type, context) + '\n'

    if not os.path.isdir(directory):
        os.makedirs(directory)

    if not os.path.isfile(full_path):
        with open(full_path, 'w') as file:
            file.write(template)


def create_solution_file(data, python):
    create_file(data, python, 'solution')


def create_test_file(data, python):
    create_file(data, python, 'test')


def main(slug, python):
    """Create new solution template"""
    access_key = get_env_variable('ACCESS_KEY')

    sys.stdout.write('Get kata data...'.ljust(STRING_LENGTH))
    data = get_kata_data(slug, access_key)
    sys.stdout.write('DONE\n')

    sys.stdout.write('Process data...'.ljust(STRING_LENGTH)),
    data = process_kata_data(data)
    sys.stdout.write('DONE\n')

    sys.stdout.write('Create solution file...'.ljust(STRING_LENGTH))
    create_solution_file(data, python)
    sys.stdout.write('DONE\n')

    sys.stdout.write('Create test file...'.ljust(STRING_LENGTH))
    create_test_file(data, python)
    sys.stdout.write('DONE\n')
