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
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    return resp.json()


def get_categories():
    """Returns a list of categories."""
    resp = requests.get(f"{URL}/api/categories/", headers=auth)
    category_names = "\n".join(category["name"] for category in resp.json())
    success_msg(category_names)
    return resp.json()


@categories.command("list")
def categories_list():
    """Returns a list of categories."""
    resp = get_categories()
    return resp


@categories.command("categorize")
@click.option(
    "-s", "--site-name", required=True, help="Enter your live site domain name"
)
def categorize_live_site(site_name):
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
    live_site_id = "".join(
        site.get("_id")
        for site in get_live_sites()
        if site_name in site.get("domain").get("Name")
    )

    resp = requests.get(
        f"{URL}/api/categorize/{live_site_id}/?category={category_name}", headers=auth
    )

    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    resp_json = resp.json()

    if resp_json.get("error"):
        error_msg(resp_json["error"])
    else:
        success_msg(resp_json["message"])

    return resp_json


@categories.command("check")
def check_categories():
    """Check a domain's categories on multiple proxies."""
    domain = input("Please enter a domain name: ")
    click.echo("Checking categories...")
    resp = requests.get(f"{URL}/api/check/?domain={domain}", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    for key, value in resp.json().items():
        success_msg(key + ": ")
        if value is not None:
            success_msg(value)
    return resp.json()
