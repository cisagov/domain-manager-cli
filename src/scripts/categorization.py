"""Check a domain's categories."""
# Third-Party Libraries
import click
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


@click.group()
def categories():
    """Manage proxy categorizations of active websites."""
    pass


def get_live_sites():
    """Returns a list of active websites."""
    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    return [site for site in resp.json() if site.get("is_active") is True]


def get_categories():
    """Returns a list of categories."""
    resp = requests.get(f"{URL}/api/categories/", headers=auth)
    category_names = "\n".join(category["name"] for category in resp.json())
    success_msg(category_names)
    return resp.json()


@categories.command("categorize")
@click.option(
    "-d", "--domain", required=True, help="Enter your active site's domain name"
)
def categorize_live_site(domain):
    """
    Categorize an active site.

    Check if the domain has already been categorized.
    Categorize the domain on multiple proxies.
    """
    # List available categories
    get_categories()

    # Choose a category
    category_name = input("Please enter a category: ")

    # Access live site data by uuid
    site_id = "".join(
        site.get("_id") for site in get_live_sites() if domain in site["name"]
    )

    resp = requests.get(
        f"{URL}/api/domain/{site_id}/categorize/?category={category_name}", headers=auth
    )

    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    success_msg(resp.text)

    return resp.text
