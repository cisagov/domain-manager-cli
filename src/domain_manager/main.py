"""Domain Manager main script."""
# Third-Party Libraries
import click
from colorama import Fore
from scripts.get_data import get_data


@click.group()
def cli():
    """Domain manager command line application."""
    pass


if __name__ == "__main__":
    header = """\
     _____                        _         __  __                                   
    |  __ \                      (_)       |  \/  |                                  
    | |  | | ___  _ __ ___   __ _ _ _ __   | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
    | |  | |/ _ \| '_ ` _ \ / _` | | '_ \  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
    | |__| | (_) | | | | | | (_| | | | | | | |  | | (_| | | | | (_| | (_| |  __/ |   
    |_____/ \___/|_| |_| |_|\__,_|_|_| |_| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                      __/ |          
                                                                     |___/           
                    Launch websites and categorize your Domains!
    """

    click.echo(Fore.CYAN + header)
    cli()
    cli.add_command(get_data)
