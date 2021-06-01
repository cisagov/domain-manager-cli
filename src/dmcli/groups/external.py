"""External domains not managed by DM."""
# Third-Party Libraries
import click

# cisagov Libraries
from dmcli.utils.categories import get_categories
from dmcli.utils.external import categorize_external, check_category
from dmcli.utils.message_handling import success_msg


@click.group()
def external():
    """Manage categorization of external websites."""
    pass


@external.command("check")
@click.option("-d", "--domain-name", required=True, prompt=True)
def check(domain_name):
    """Check category on an unmanaged website."""
    resp = check_category(domain_name)
    for proxy in resp:
        success_msg("\n".join(f"{key}: {value}" for key, value in proxy.items()))


@external.command("categorize")
@click.option("-d", "--domain-name", required=True, prompt=True)
def categorize(domain_name):
    """Categorize an unmanaged website."""
    categories = get_categories()
    category_name = click.prompt(
        "Please enter a category", type=click.Choice(categories)
    )
    resp = categorize_external(domain_name, category_name)
    for proxy in resp:
        success_msg("\n".join(f"{key}: {value}" for key, value in proxy.items()))
