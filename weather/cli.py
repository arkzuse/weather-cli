import click
from simple_term_menu import TerminalMenu
from weather.core import search
from weather.utils import make_name, get_default_location, set_default_location


@click.command()
@click.argument('place', default=get_default_location(), required=False)
def main(place):
    if place == '':
        click.echo('Default place not set.')

        new_default = click.prompt('Enter a default place')

        set_default_location(new_default)
        place = new_default

    search_result = search(place)

    if len(search_result) == 0:
        click.echo('No results found')
        return

    selected = 0

    if len(search_result) > 1:
        names = [make_name(obj) for obj in search_result]
        selected = TerminalMenu(names).show()

    place = search_result[selected]['url']

    print(place)
