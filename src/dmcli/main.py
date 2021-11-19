"""Domain Manager main script."""
# Third-Party Libraries
import click

# cisagov Libraries
from dmcli.groups.application import application
from dmcli.groups.category import category
from dmcli.groups.configure import configure
from dmcli.groups.domain import domain
from dmcli.groups.external import external
from dmcli.groups.record import record
from dmcli.groups.template import template
from dmcli.utils.message_handling import info_msg

from ._version import __version__

HEADER = """\
____                    _         _____
|    \\  ___  _____  ___ |_| ___   |     | ___  ___  ___  ___  ___  ___
|  |  || . ||     || .'|| ||   |  | | | || .'||   || .'|| . || -_||  _|
|____/ |___||_|_|_||__,||_||_|_|  |_|_|_||__,||_|_||__,||_  ||___||_|
                                                    |___|
"""

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option(__version__)
@click.pass_context
def cli(ctx):
    """Domain manager command line application."""
    if ctx.invoked_subcommand is None:
        info_msg(HEADER)
        print(ctx.command.get_help(ctx))
    pass


def start():
    """Run cli."""
    # add command groups to the cli
    cli.add_command(application)
    cli.add_command(category)
    cli.add_command(configure)
    cli.add_command(domain)
    cli.add_command(external)
    cli.add_command(record)
    cli.add_command(template)

    # Run the command line application
    cli()


if __name__ == "__main__":
    start()
