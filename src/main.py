"""Domain Manager main script."""
# Third-Party Libraries
import click
from scripts.categorization import categories
from scripts.get_data import get_data
from scripts.manage_sites import manage_sites
from utils.message_handling import info_msg

HEADER = """\
____                    _         _____                               
|    \  ___  _____  ___ |_| ___   |     | ___  ___  ___  ___  ___  ___ 
|  |  || . ||     || .'|| ||   |  | | | || .'||   || .'|| . || -_||  _|
|____/ |___||_|_|_||__,||_||_|_|  |_|_|_||__,||_|_||__,||_  ||___||_|  
                                                    |___|          
"""

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Domain manager command line application."""
    if ctx.invoked_subcommand is None:
        info_msg(HEADER)
        print(ctx.command.get_help(ctx))
    pass


def start():
    """The main method called by __main__."""
    # add command groups to the cli
    cli.add_command(get_data)
    cli.add_command(manage_sites)
    cli.add_command(categories)

    # Run the command line application
    cli()


if __name__ == "__main__":
    start()
