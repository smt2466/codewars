import click

from utils import new_solution


@click.group()
def main():
    pass


@main.command()
@click.argument('slug')
@click.argument('python')
def new(slug, python):
    new_solution.main(slug, python)

if __name__ == '__main__':
    main()
