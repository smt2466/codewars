import click


@click.group()
def main():
    pass


@main.command()
@click.argument('slug')
def new(slug):
    click.echo('Start new... %s' % slug)

if __name__ == '__main__':
    main()
