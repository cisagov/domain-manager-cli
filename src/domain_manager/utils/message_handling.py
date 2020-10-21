"""Return messages handler."""
# Third-Party Libraries
import click
from colorama import Fore


def success_msg(text):
    """Success message."""
    click.echo(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    """Error message."""
    click.echo(Fore.LIGHTRED_EX + text + Fore.WHITE)


def unknown_command():
    """Unknown command response."""
    click.echo("Sorry we didn't understand that command.")
