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
 ____                    _         _____                               
|    \  ___  _____  ___ |_| ___   |     | ___  ___  ___  ___  ___  ___ 
|  |  || . ||     || .'|| ||   |  | | | || .'||   || .'|| . || -_||  _|
|____/ |___||_|_|_||__,||_||_|_|  |_|_|_||__,||_|_||__,||_  ||___||_|  
                                                        |___|          
    """
    click.echo(Fore.CYAN + header)

    # add command groups to the cli
    cli.add_command(get_data)
    cli()
