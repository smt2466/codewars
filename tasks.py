import os
import sys

from invoke import task

from utils.utils import get_python_version, new_solution, sort_katas


@task
def check_venv(ctx):
    pyenv = os.environ.get('PYENV_VIRTUAL_ENV', False)
    virtualenv = hasattr(sys, 'real_prefix')
    if not virtualenv and not pyenv:
        raise EnvironmentError('Activate virtual environment before!')


@task(check_venv)
def update(ctx):
    """Updates virtual environments"""
    python2 = '~/.pyenv/versions/codewars2/bin'
    python3 = '~/.pyenv/versions/codewars3/bin'

    ctx.run('pur -r requirements.txt')
    ctx.run('{}/pip install -r requirements.txt'.format(python2))
    ctx.run('{}/pip install -r requirements.txt'.format(python3))


@task(check_venv)
def sort(ctx):
    """Sorts kata"""
    sort_katas()


@task(check_venv)
def new(ctx, slug):
    python = get_python_version()
    new_solution(slug, python)


@task(check_venv)
def test(ctx):
    python = get_python_version()
    ctx.run('python -m pytest --doctest-modules {0} tests/{0}'.format(python))


@task(check_venv)
def syntax(ctx):
    python = get_python_version()
    ctx.run('python -m pylint {0} tests/{0}'.format(python))
