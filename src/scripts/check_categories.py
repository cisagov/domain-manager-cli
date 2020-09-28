"""Check a domain's categories."""
# Third-Party Libraries
from colorama import Fore
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


def check_categories():
    """Check a domain's categories on multiple proxies."""
    domain = input("Please enter a domain name: ")
    resp = requests.get(f"{URL}/api/check/?domain={domain}", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    for key, value in resp.json().items():
        print(Fore.GREEN + key + ": " + Fore.WHITE)
        if value is not None:
            success_msg(value)
    return resp.json()
