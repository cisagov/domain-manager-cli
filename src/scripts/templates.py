"""Template CLI commands."""
# Third-Party Libraries
import click
import requests
from utils.message_handling import error_msg, success_msg
from utils.settings import URL, auth


@click.group()
def manage_templates():
    """Manage go templates."""
    pass


@manage_templates.command("upload")
@click.option("-f", "--filename", required=True, help="Enter your .zip filename.")
def upload_template(filename):
    """Upload a zipped template file."""
    with open(f"./src/uploads/{filename}", "rb") as zip_file:
        content = zip_file.read()
        resp = requests.post(
            f"{URL}/api/templates/", files={"zip": (filename, content)}, headers=auth
        )
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            error_msg(str(e))
            return
        success_msg(f"{filename} template has been uploaded")
        return resp.json()
