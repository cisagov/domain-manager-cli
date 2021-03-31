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


@get_data.command("domains")
def get_domains():
    """Returns all domains."""
    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    domains = [domain.get("name") for domain in resp.json()]
    success_msg("\n".join(domains))
    return resp.json()


@get_data.command("active-sites")
def get_active_sites():
    """Returns domains that are currently live."""
    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    sites = [site.get("name") for site in resp.json() if site.get("is_active") is True]
    success_msg("\n".join(sites))
    return resp.json()


@get_data.command("inactive-sites")
def get_inactive_sites():
    """Returns domains that are available for use."""
    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    sites = [site.get("name") for site in resp.json() if site.get("is_active") is False]
    success_msg("\n".join(sites))
    return resp.json()


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
