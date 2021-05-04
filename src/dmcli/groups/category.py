"""Category CLI."""
# Third-Party Libraries
import click

# cisagov Libraries
from utils.categories import get_categories
from utils.message_handling import success_msg


@click.group()
def category():
    """Manage categories CLI group."""
    pass


@category.command("all")
def all():
    """Get categories from CLI."""
    categories = [category for category in get_categories()]
    success_msg("\n".join(categories))
