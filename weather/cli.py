import click
from simple_term_menu import TerminalMenu
from weather.core import search
from weather.utils import make_name, get_default_location, set_default_location


def handle_no_default():
    click.echo('Default place not set!')

    new_default = click.prompt('Enter a default place')

    set_default_location(new_default)

    return new_default


@click.command()
@click.argument('place', default=get_default_location(), required=False)
def main(place):
    selected = 0

    if place == '':
        place = handle_no_default()

    search_result = search(place)

    if len(search_result) == 0:
        click.echo('No results found')
        return

    if len(search_result) > 1:
        names = [make_name(obj) for obj in search_result]
        selected = TerminalMenu(names).show()

    place = search_result[selected]['url']

    print(place)
