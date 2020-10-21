"""DNS record handler."""
# Third-Party Libraries
import click
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


@click.group()
def hosted_zones():
    """Manage AWS Route53 Hosted Zones for registered domains."""
    pass


@hosted_zones.command("generate")
@click.option("-f", "--filename", help="Enter your .txt filename.")
def generate_hosted_zones(filename):
    """Generate Route53 Hosted Zones for specified domains."""
    post_data = {}
    with open(f"../../text_files/{filename}", "r") as reader:
        post_data["domains"] = [line.replace("\n", "") for line in reader]

    resp = requests.post(f"{URL}/api/generate-dns/", headers=auth, json=post_data)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    resp_txt = "\n\n".join(
        key + "\n\n" + "\n".join(value) for key, value in resp.json().items()
    )
    with open("output.txt", "w") as output:
        output.write(resp_txt)

    success_msg(
        "DNS handlers have been created for: \n" + "\n".join(i for i in resp.json())
    )
    success_msg("\nPlease check output.txt to retrieve your nameservers")
    return resp.json()
