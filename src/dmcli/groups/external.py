"""External CLI."""
# Third-Party Libraries
import click

# cisagov Libraries
from dmcli.utils.categories import get_categories
from dmcli.utils.external import (
    categorize_external_domain,
    create_external_domain,
    delete_external_domain,
    get_external_domain_categories,
    get_external_domains,
)
from dmcli.utils.message_handling import success_msg, warning_msg


@click.group()
def external():
    """Manage external domains CLI group."""
    pass


@external.command("all")
def all():
    """Get all external domains."""
    return success_msg("\n".join([domain["name"] for domain in get_external_domains()]))


@external.command("domain")
@click.option("-d", "--domain", required=True, prompt=True)
def details(domain):
    """Get external domain details including categorization."""
    domain_details = get_external_domains(domain_name=domain)[0]
    cat_details = get_external_domain_categories(domain_details["_id"])
    return success_msg(
        "\n".join(
            f"{key}: {value}"
            for key, value in domain_details.items()
            if value is not None and key not in ["_id", "updated", "updated_by"]
        )
        + "\n"
        + "\n".join(f"{cat['proxy']}: {cat['status']}" for cat in cat_details)
    )


@external.command("categorize")
@click.option("-d", "--domain", required=True, prompt=True)
@click.option("-e", "--email", required=True, prompt=True)
def categorize(domain, email):
    """Categorize a new external domain."""
    domain = create_external_domain(domain, email)
    if domain["message"]:
        warning_msg(domain["message"])
        return
    categories = get_categories()
    category_name = click.prompt(
        "Please enter a category", type=click.Choice(categories)
    )
    resp = categorize_external_domain(domain["_id"], category_name)
    return success_msg(resp.get("success"))


@external.command("delete")
@click.option("-d", "--domain", required=True, prompt=True)
def delete(domain):
    """Delete an external domain."""
    external_domain = get_external_domains(domain)
    delete_external_domain(external_domain[0]["_id"])
    return success_msg(f"{domain} has been deleted.")
