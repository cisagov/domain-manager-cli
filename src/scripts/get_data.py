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


@get_data.command("domains")
def get_domains():
    """Returns a list of domains."""
    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    domains = [domain.get("name") for domain in resp.json()]
    success_msg("\n".join(domains))
    return resp.json()


@get_data.command("live-sites")
def get_live_sites():
    """Returns a list of domains that are currently live."""
    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    sites = [site.get("name") for site in resp.json() if site.get("is_active") is True]
    success_msg("\n".join(sites))
    return resp.json()


@get_data.command("users")
def get_users():
    """Returns a list of users."""
    resp = requests.get(f"{URL}/api/users/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    users = [user.get("Username") for user in resp.json()]
    success_msg("\n".join(users))
    return resp.json()
