"""Templates CLI."""
# Third-Party Libraries
import click

# cisagov Libraries
from dmcli.utils.message_handling import success_msg
from dmcli.utils.templates import get_templates, upload_template


@click.group()
def template():
    """Manage templates CLI group."""
    pass


@template.command("all")
def all():
    """Get templates from CLI."""
    templates = [template.get("name") for template in get_templates()]
    success_msg("\n".join(templates))


@template.command("upload")
@click.option("-f", "--filepath", required=True, prompt=True, type=str)
def upload(filepath):
    """Upload a zipped template file."""
    resp = upload_template(filepath)
    if resp:
        success_msg(f"{filepath} template has been uploaded")
