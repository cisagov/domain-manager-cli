"""A sample python script."""
# Third-Party Libraries
from colorama import Fore
import requests
from utils.settings import URL, auth


def get_domain_list():
    """Returns a list of available domains from Route53."""
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    live_sites = [site.get("name") + "." for site in resp.json()]

    resp = requests.get(f"{URL}/api/domains/", headers=auth)
    domains = [
        domain.get("Name")
        for domain in resp.json()
        if not domain.get("Name") in live_sites
    ]

    print(
        Fore.GREEN
        + """
**** Domains ****
    """
    )
    print(Fore.GREEN + "\n".join(domains))
    return resp.json()


def get_website_content_list():
    """Returns a list of available website content from S3."""
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    live_site_contents = [site.get("website").get("name") for site in resp.json()]

    resp = requests.get(f"{URL}/api/websites/", headers=auth)
    content = [
        content.get("name")
        for content in resp.json()
        if not content.get("name") in live_site_contents
    ]

    print(
        Fore.GREEN
        + """
**** Website Content ****
    """
    )
    print(Fore.GREEN + "\n".join(content))
    return resp.json()


def get_application_list():
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
    print(
        Fore.GREEN
        + """
**** Applications ****
    """
    )
    print(Fore.GREEN + "\n".join(applications))
    return resp.json()


def get_live_site_list():
    """Returns a list of active websites."""
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    live_sites = [site.get("name") for site in resp.json()]
    print(
        Fore.GREEN
        + """
    **** Live Sites ****
    """
    )
    print(Fore.GREEN + "\n".join(live_sites))
    return resp.json()
