import click

from utils import new_solution


@click.group()
def main():
    pass


@main.command()
@click.argument('slug')
def new(slug):
    new_solution.main(slug)

if __name__ == '__main__':
    main()
