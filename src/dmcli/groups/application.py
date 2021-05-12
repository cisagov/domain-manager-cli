"""Application CLI."""
# Third-Party Libraries
import click

# cisagov Libraries
from dmcli.utils.application import get_applications
from dmcli.utils.message_handling import success_msg


@click.group()
def application():
    """Manage applications CLI group."""
    pass


@application.command("all")
def all():
    """Get applications from CLI."""
    applications = [application.get("name") for application in get_applications()]
    success_msg("\n".join(applications))
