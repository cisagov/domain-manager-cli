"""A sample python script."""
# Third-Party Libraries
import click
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


@click.group()
def get_data():
    """Get available data."""
    pass


@get_data.command("applications")
def get_applications():
    """Returns a list of applications."""
    resp = requests.get(f"{URL}/api/applications/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    applications = [application.get("name") for application in resp.json()]
    success_msg("\n".join(applications))
    return resp.json()


@get_data.command("categories")
def get_categories():
    """Return all categories for proxy submission."""
    resp = requests.get(f"{URL}/api/categories/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    categories = [category for category in resp.json()]
    success_msg("\n".join(categories))
    return resp.json()


def get_domains_list():
    """Return all domains."""
    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


@get_data.command("domains")
def get_domains():
    """Returns all domains."""
    domains = [domain.get("name") for domain in get_domains_list()]
    success_msg("\n".join(domains))


@get_data.command("active-sites")
def get_active_sites():
    """Returns domains that are currently live."""
    sites = [
        site.get("name") for site in get_domains_list() if site.get("is_active") is True
    ]
    sites.sort()
    success_msg("\n".join(sites))


@get_data.command("inactive-sites")
def get_inactive_sites():
    """Returns domains that are available for use."""
    sites = [
        site.get("name")
        for site in get_domains_list()
        if site.get("is_active") is False
    ]
    sites.sort()
    success_msg("\n".join(sites))


@get_data.command("nameservers")
@click.option("-d", "--domain", required=True, help="Enter a domain name")
def get_nameservers(domain):
    """Returns a domain's nameservers."""
    domain_id = "".join(x["_id"] for x in get_domains_list() if x["name"] == domain)

    resp = requests.get(f"{URL}/api/domain/{domain_id}/records/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    success_msg(
        "\n".join(record["Value"] for record in resp.json()[0]["ResourceRecords"])
    )


@get_data.command("templates")
def get_templates():
    """Returns all templates."""
    resp = requests.get(f"{URL}/api/templates/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    templates = [template.get("name") for template in resp.json()]
    success_msg("\n".join(templates))
    return resp.json()
