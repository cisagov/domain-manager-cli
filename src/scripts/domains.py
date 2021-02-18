"""A sample python script."""
# Third-Party Libraries
import click
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


@click.group()
def manage_sites():
    """Manage domains and websites."""
    pass


def get_sites(active=False):
    """Returns active domains."""
    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    if active:
        return [site for site in resp.json() if site.get("is_active") is True]
    else:
        return [site for site in resp.json() if site.get("is_active") is False]


@manage_sites.command("upload")
@click.option("-d", "--domain-name", required=True, help="Enter your domain name")
@click.option("-f", "--filename", required=True, help="Enter your .zip filename.")
def upload_website(domain_name, filename):
    """Upload a zipped website file."""
    site_id = "".join(
        site["_id"] for site in get_sites(active=False) if domain_name == site["name"]
    )
    with open(f"./src/uploads/{filename}", "rb") as zip_file:
        content = zip_file.read()
        resp = requests.post(
            f"{URL}/api/domain/{site_id}/content/?category={filename}",
            files={"zip": (filename, content)},
            headers=auth,
        )
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            error_msg(str(e))
            return
        success_msg(f"{filename} has been uploaded to {domain_name}")
        return resp.json()


@manage_sites.command("delete")
@click.option("-d", "--domain-name", required=True, help="Enter your domain name")
def delete_website(domain_name):
    """Delete content from a domain."""
    site_id = "".join(
        site["_id"] for site in get_sites(active=False) if domain_name == site["name"]
    )
    resp = requests.delete(
        f"{URL}/api/domain/{site_id}/content/",
        headers=auth,
    )
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    success_msg(f"Content has been deleted from {domain_name}")
    return resp.json()


@manage_sites.command("launch")
@click.option("-d", "--domain-name", required=True, help="Enter your domain name")
def launch_site(domain_name):
    """Launch an inactive website."""
    # Access inactive site data by uuid
    site_id = "".join(
        site["_id"] for site in get_sites(active=False) if domain_name == site["name"]
    )

    click.echo(
        click.style("launching... this may take up to a few minutes.", fg="yellow")
    )

    resp = requests.get(f"{URL}/api/domain/{site_id}/launch/", headers=auth)

    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    success_msg(resp.json()["success"])
    return resp.json()


@manage_sites.command("takedown")
@click.option("-d", "--domain-name", required=True, help="Enter your domain name")
def takedown_site(domain_name):
    """Takedown an active website."""
    # Access active site data by uuid
    site_id = "".join(
        site["_id"] for site in get_sites(active=True) if domain_name == site["name"]
    )

    click.echo(
        click.style("deleting... this may take up to a few minutes.", fg="yellow")
    )

    resp = requests.delete(f"{URL}/api/domain/{site_id}/launch/", headers=auth)

    success_msg(f"{domain_name} is now inactive")
    return resp.json()
