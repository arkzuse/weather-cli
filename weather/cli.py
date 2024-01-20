import click
from simple_term_menu import TerminalMenu
from weather.core import search
from weather.utils import make_name, get_default_location


@click.command()
@click.argument('place', default=get_default_location(), required=False)
def main(place):
    places = search(place)
    names = [make_name(obj) for obj in places]
    selected = TerminalMenu(names).show()
    print(names[selected])
