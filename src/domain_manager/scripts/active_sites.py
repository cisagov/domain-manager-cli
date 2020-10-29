"""A sample python script."""
# Third-Party Libraries
import click
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


@click.group()
def active_sites():
    """Manage active site."""
    pass


def get_domains():
    """Returns a list of available domains from Route53."""
    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    return resp.json()


def get_website_content():
    """Returns a list of available website content from S3."""
    resp = requests.get(f"{URL}/api/websites/", headers=auth)
    return resp.json()


def get_applications():
    """Returns a list of applications."""
    resp = requests.get(f"{URL}/api/applications/", headers=auth)
    return resp.json()


def get_live_sites():
    """Returns a list of active websites."""
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    return resp.json()


@active_sites.command("launch")
@click.option("-d", "--domain-name", required=True, help="Enter your domain name")
def launch_live_site(domain_name):
    """
    Launch a live website.

    Input data accessed by name.
    Application that will be using active site.
    A Registered Domain.
    Website content URL.
    """
    domain_name = f"{domain_name}"
    # Access data by their uuids
    domain_id = "".join(
        domain.get("_id")
        for domain in get_domains()
        if domain_name == domain.get("Name")
    )

    use_ip = input("Utilize an existing IP address? [Y]es or [N]o ")

    application_name = input("Please enter an available application name: ")
    application_id = "".join(
        application.get("_id")
        for application in get_applications()
        if application_name == application.get("name")
    )

    post_data = {
        "application_id": application_id,
        "domain_id": domain_id,
    }

    if use_ip == "y":
        ip_address = input("Please enter your IP address: ")
        post_data["ip_address"] = ip_address
    else:
        content_name = input("Please enter available content name: ")

        content_id = "".join(
            content.get("_id")
            for content in get_website_content()
            if content_name == content.get("name")
        )
        post_data["website_id"] = content_id

    click.echo(
        click.style("launching... this may take up to a few minutes.", fg="yellow")
    )

    resp = requests.post(f"{URL}/api/live-sites/", headers=auth, json=post_data)

    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    success_msg(resp.json()["message"])
    return resp.json()


@active_sites.command("delete")
@click.option("-d", "--domain-name", required=True, help="Enter your domain name")
def delete_live_site(domain_name):
    """
    Deactivate an active site.

    Unhook domain name by removing DNS records.
    Delete the live S3 bucket if applicable.
    """
    # Access live site data by uuid
    live_site_id = "".join(
        site.get("_id") for site in get_live_sites() if domain_name == site.get("name")
    )

    resp = requests.delete(f"{URL}/api/live-site/{live_site_id}/", headers=auth)
    success_msg(resp.json()["message"])
    return resp.json()
