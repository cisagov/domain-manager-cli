import click
from utils.application import get_applications
from utils.message_handling import success_msg


@click.group()
def application():
    """Manage applications CLI group."""
    pass


@application.command("all")
def all():
    """Get applications from CLI."""
    applications = [application.get("name") for application in get_applications()]
    success_msg("\n".join(applications))