"""A sample python script."""
# Third-Party Libraries
import click
from colorama import Fore
import requests
from utils.settings import URL, auth


@click.group()
def get_data():
    """Get available data."""
    pass


@get_data.command("domains")
def get_domains():
    """Returns a list of available domains from Route53."""
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    live_sites = [site.get("name") + "." for site in resp.json()]

    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    domains = [
        domain.get("Name")
        for domain in resp.json()
        if not domain.get("Name") in live_sites
    ]
    print(Fore.GREEN + "\n".join(domains))
    return resp.json()


@get_data.command("content")
def get_website_content():
    """Returns a list of available website content from S3."""
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    live_site_contents = [site.get("website").get("name") for site in resp.json()]

    resp = requests.get(f"{URL}/api/websites/", headers=auth)
    content = [
        content.get("name")
        for content in resp.json()
        if not content.get("name") in live_site_contents
    ]
    click.echo(Fore.GREEN + "\n".join(content))
    return resp.json()


@get_data.command("applications")
def get_applications():
    """Returns a list of applications."""
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    live_site_applications = [
        site.get("application").get("name") for site in resp.json()
    ]

    resp = requests.get(f"{URL}/api/applications/", headers=auth)
    applications = [
        application.get("name")
        for application in resp.json()
        if not application.get("name") in live_site_applications
    ]
    click.echo(Fore.GREEN + "\n".join(applications))
    return resp.json()


@get_data.command("live-sites")
def get_live_sites():
    """Returns a list of active websites."""
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    live_sites = [site.get("name") for site in resp.json()]
    click.echo(Fore.GREEN + "\n".join(live_sites))
    return resp.json()
