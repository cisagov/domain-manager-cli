"""A sample python script."""
# Standard Python Libraries
import os

# Third-Party Libraries
from dotenv import load_dotenv
import requests
from utils.message_handling import success_msg

# Load environment variables from .env file
load_dotenv()
URL = os.environ.get("API_URL")
API_KEY = os.environ.get("API_KEY")

# Pass in api key for authorized access
auth = {"api_key": API_KEY}


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


def launch_live_site():
    """
    Launch a live website.

    Input data accessed by name.
    Application that will be using active site.
    A Registered Domain.
    Website content URL.
    """
    use_ip = input("Utilize an existing IP address? [Y]es or [N]o ")
    domain_name = input("Please enter an available domain name: ")
    application_name = input("Please enter an available application name: ")
    domain_name = f"{domain_name}."
    # Access data by their uuids
    domain_id = "".join(
        domain.get("_id")
        for domain in get_domains()
        if domain_name == domain.get("Name")
    )

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

    resp = requests.post(f"{URL}/api/live-sites/", headers=auth, json=post_data)

    success_msg(resp.json())
    return resp.json()


def delete_live_site(live_site_id):
    """
    Deactivate an active site.

    Unhook domain name by removing DNS records.
    Delete the live S3 bucket if applicable.
    """
    resp = requests.delete(f"{URL}/api/live-site/{live_site_id}/", headers=auth)

    return resp.json()
