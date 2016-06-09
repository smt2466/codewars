"""Generate new kata solution and tests template"""

import os

from jinja2 import Environment, FileSystemLoader
import requests

STRING_LENGTH = 50

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    loader=FileSystemLoader(os.path.join(PATH, 'templates')))


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


def create_solution_file(data, python):
    description = data['description']
    name = data['name']
    slug = data['slug']
    rank = str(abs(data['rank']['id']))
    url = data['url']

    filename = slug.replace('-', '_') + '.py'
    full_path = os.path.join('python' + python, 'kyu_' + rank, filename)

    context = {
        'kata': {
            'title': name,
            'python': python,
            'filename': filename,
            'url': url,
            'description': description,
            'rank': rank,
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
