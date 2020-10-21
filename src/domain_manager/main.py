"""Domain Manager main script."""
# Third-Party Libraries
import click
from colorama import Fore
from scripts.active_sites import active_sites
from scripts.categorization import categories
from scripts.dns_record_handler import hosted_zones
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
    cli.add_command(hosted_zones)
    cli.add_command(active_sites)
    cli.add_command(categories)

    # Run the command line application
    cli()
