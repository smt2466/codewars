"""Rearrange solutions and tests by ranks

Read more about the script in the repository README
"""

import os
import re
from itertools import repeat
from os.path import isfile, join

import concurrent.futures
import requests

STRING_LENGTH = 44
SLUG_PATTERN = re.compile(r'.*/kata/([^/]*)')


def get_env_variable(var_name):
    """Get environment variable or raise exceptions"""
    try:
        return os.environ[var_name]
    except KeyError:
        raise KeyError('%s environment variable is not set' % var_name)


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

if __name__ == '__main__':
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

    # Codewars API key from environment variable
    print('Getting codewars access key...'.ljust(STRING_LENGTH)),
    access_key = get_env_variable('ACCESS_KEY')
    print('DONE')

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
            executor.map(get_rank, slugs.values(), repeat(access_key))
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
