"""DNS record handler."""
# Third-Party Libraries
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


def generate_hosted_zones():
    """Generate Route53 Hosted Zones for specified domains."""
    post_data = {
        "domains": ["signalsquared.com", "signalcubed.com", "signalpowerthree.com"]
    }
    resp = requests.post(f"{URL}/api/generate-dns/", headers=auth, json=post_data)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    success_msg(
        "DNS handlers have been created for \n" + "\n".join(i for i in resp.json())
    )
    return resp.json()
