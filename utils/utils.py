import concurrent.futures
import os
import re
import sys
from collections import namedtuple
from itertools import repeat
from os.path import isfile, join

import requests
from jinja2 import Environment, FileSystemLoader

from .envs import ACCESS_KEY

STRING_LENGTH = 44
SLUG_PATTERN = re.compile(r'.*/kata/([^/]*)')
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    loader=FileSystemLoader(os.path.join(PATH, 'templates')))

Kata = namedtuple('Kata', 'name url slug rank description')


def get_python_version():
    if sys.version.startswith('3'):
        return 'python3'
    elif sys.version.startswith('2'):
        return 'python2'
    else:
        raise EnvironmentError('Unknown Python version')


def get_kata_slug(kata_name, directory):
    """Get kata id or slug from solution file"""
    with open(join(directory, kata_name)) as solution:
        for solution_line in solution.readlines():
            match = SLUG_PATTERN.match(solution_line)
            if match:
                return match.groups()[0].rstrip()


def creates_kyu_folders(parent_path):
    """Create sub folders to store solutions and tests"""
    for i in range(1, 9):
        directory_path = join(parent_path, 'kyu_%d' % i)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            with open(join(parent_path, directory_path, '__init__.py'), 'w'):
                pass


def get_rank(kata_slug, api_key):
    """Send request to Codewars API and extract rank"""
    url = 'https://www.codewars.com/api/v1/code-challenges/%s' % kata_slug
    params = {'access_key': api_key}
    response = requests.get(url, params)
    if response.status_code == 200:
        data = response.json()
        kata_rank = abs(int(data['rank']['id']))
        return kata_rank
    else:
        raise Exception(response)


def sort_katas():
    """Sort katas"""
    # Paths for solutions and tests
    src_path = os.path.realpath('../src')
    tests_path = os.path.realpath('../tests')

    # New directories to store solutions and tests
    print('Create sub directories for kata solutions...'.ljust(STRING_LENGTH)),
    creates_kyu_folders(src_path)
    creates_kyu_folders(tests_path)
    print('DONE')

    # Read solutions and tests files
    print('Read files...'.ljust(STRING_LENGTH)),
    katas = [f for f in os.listdir(src_path) if isfile(join(src_path, f))
             if f != '__init__.py']
    tests = [f for f in os.listdir(tests_path) if isfile(join(tests_path, f))
             if f != '__init__.py']
    print('DONE')
    print('    - Solutions: %d files' % len(katas))
    print('    - Tests: %d files' % len(tests))
    if len(katas) != len(tests):
        print('WARNING: number of solutions is not equal to number of tests!')

    # Extract kata slug from solutions files
    print('Process files for slug...'.ljust(STRING_LENGTH)),
    slugs = {kata: get_kata_slug(kata, src_path) for kata in katas}
    print('DONE')

    # Connect to Codewars and receive kata ranks
    print('Send requests to codewars API...'.ljust(STRING_LENGTH)),
    ranks = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for kata, rank in zip(
                slugs.keys(),
                executor.map(get_rank, slugs.values(), repeat(ACCESS_KEY))
        ):
            ranks[kata] = rank
    print('DONE')

    # Move files according of rank
    print('Rearrange files...'.ljust(STRING_LENGTH))
    for kata, rank in ranks.items():
        # Solution file
        source = join(src_path, kata)
        destination = join(src_path, 'kyu_%d' % rank, kata)
        os.rename(source, destination)

        # Test file (move and fix imports)
        source = join(tests_path, 'test_' + kata)
        destination = join(tests_path, 'kyu_%d' % rank, 'test_' + kata)
        try:
            with open(source, 'r') as old_file,\
                 open(destination, 'w') as new_file:
                for line in old_file:
                    new_file.write(line.replace('from src.',
                                                'from src.kyu_%d.' % rank))
            os.remove(source)
        except OSError:
            print('Can not find test file: %s' % source)

    print('\nComplete!')


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def get_kata_data(slug, access_key):
    """Get kata data"""
    url = 'https://www.codewars.com/api/v1/code-challenges/%s' % slug
    params = {'access_key': access_key}
    response = requests.get(url, params)

    if response.status_code != 200:
        sys.stdout.write('ERROR\n')
        raise ValueError('Can not retrieve kata data from the server!')
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


def new_solution(slug, python):
    """Create new solution template"""
    sys.stdout.write('Get kata data...'.ljust(STRING_LENGTH))
    data = get_kata_data(slug, ACCESS_KEY)
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
