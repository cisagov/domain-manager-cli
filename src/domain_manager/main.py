"""Domain Manager main script."""
# Third-Party Libraries
import click
from colorama import Fore


@click.group()
def main():
    """Entrypoint group."""
    pass


@main.group()
def get_data():
    """Return domain manager data."""
    pass


@get_data.command("domains")
def get_domains():
    """Get a list of domains."""
    pass


@get_data.command("content")
def get_content():
    """Get a list of content."""
    click.echo("get_content")


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
    main()
