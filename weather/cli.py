import click
from simple_term_menu import TerminalMenu
from weather.core import search


@click.command()
def main():
    places = search('panki')
