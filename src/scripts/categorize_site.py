"""A sample python script."""
# Third-Party Libraries
from colorama import Fore
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


def get_live_sites():
    """Returns a list of active websites."""
    resp = requests.get(f"{URL}/api/live-sites/", headers=auth)
    return resp.json()


def get_categories():
    """Returns a list of categories."""
    resp = requests.get(f"{URL}/api/categories/", headers=auth)
    return resp.json()


def categorize_live_site():
    """
    Categorize an active site.

    Check if the domain has already been categorized.
    Categorize the domain on multiple proxies.
    """
    # Define the desired site name from list
    site_name = input("Please enter site name: ")

    categories = [category.get("name") for category in get_categories()]

    print(Fore.LIGHTBLUE_EX + "\n".join(categories) + Fore.WHITE)

    # Choose a category
    category_name = input("Please enter a category: ")
    print(category_name)
    # Access live site data by uuid
    live_site_id = "".join(
        site.get("_id")
        for site in get_live_sites()
        if site_name == site.get("domain").get("Name")
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
