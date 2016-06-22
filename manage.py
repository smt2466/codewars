import click

from utils import new_solution


@click.group()
def main():
    pass


@main.command()
@click.argument('slug')
@click.argument('python')
def new(slug, python):
    if python not in ['python2', 'python3']:
        raise ValueError('Incorrect python version!')
    new_solution.main(slug, python)

if __name__ == '__main__':
    main()
