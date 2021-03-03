"""External domains not managed by DM."""
# Third-Party Libraries
import click
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


@click.group()
def external():
    """Manage categorization of external websites."""
    pass


@external.command("check")
@click.option("-d", "--domain", required=True, help="Enter a domain name")
def check_category(domain):
    """Check category on an unmanaged website."""
    resp = requests.get(f"{URL}/api/categories/{domain}/external/", headers=auth)

    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    for proxy in resp.json():
        success_msg("".join(f"{key}: {value}" for key, value in proxy.items()))
    return resp.text


@external.command("categorize")
@click.option("-d", "--domain", required=True, help="Enter a domain name")
@click.option("-c", "--category", required=True, help="Enter a proxy category")
def categorize(domain, category):
    """Categorize an unmanaged website."""
    resp = requests.post(
        f"{URL}/api/categories/{domain}/external/",
        json={"category": category},
        headers=auth,
    )

    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    success_msg(resp.text)
    return resp.text
