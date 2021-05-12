"""Domain CLI."""
# Third-Party Libraries
import click

# cisagov Libraries
from dmcli.utils.application import get_applications
from dmcli.utils.categories import get_categories
from dmcli.utils.domain import (
    categorize_site,
    delete_content,
    generate_content,
    get_domain,
    get_domains,
    get_hosted_zone,
    launch_site,
    proxy_category_check,
    takedown_site,
    upload_content,
)
from dmcli.utils.message_handling import success_msg, warning_msg
from dmcli.utils.templates import get_templates, template_attributes


@click.group()
def domain():
    """Manage domains CLI group."""
    pass


@domain.command("all")
@click.option("-g", "--group", required=False, help="Application Name", type=str)
def all(group):
    """Get all assigned domains."""
    if group:
        application = get_applications(params=f"name={group}")[0]
        domains = get_domains(params=f"application_id={application['_id']}")
    else:
        domains = get_domains()
    success_msg("\n".join([domain["name"] for domain in domains]))


@domain.command("active")
def active():
    """Get active sites."""
    domains = get_domains()
    success_msg(
        "\n".join([domain["name"] for domain in domains if domain.get("is_active")])
    )


@domain.command("inactive")
def inactive():
    """Get inactive sites."""
    domains = get_domains()
    success_msg(
        "\n".join([domain["name"] for domain in domains if not domain.get("is_active")])
    )


@domain.command("hostedzone")
@click.option("-d", "--domain", required=True, prompt=True)
def hostedzone(domain):
    """Get domain's hosted zone from route53."""
    domain = get_domain(domain)
    hostedzone = get_hosted_zone(domain)
    msg = ["\n"]
    for record in hostedzone:
        msg.append(f"Name: {record['Name']}")
        msg.append(f"Type: {record['Type']}")

        if record.get("AliasTarget"):
            alias = record["AliasTarget"]
            msg.append("AliasTarget:")
            msg.append(f"\tDNSName: {alias['DNSName']}")
            msg.append(f"\tEvaluateTargetHealth: {alias['EvaluateTargetHealth']}")
            msg.append(f"\tHostedZoneId: {alias['HostedZoneId']}")
        else:
            msg.append(f"TTL: {record['TTL']}")
            msg.append("Values:")
            for value in record["ResourceRecords"]:
                msg.append(f"\t{value['Value']}")
        msg.append("\n")
    success_msg("\n".join(msg))


@domain.command("nameservers")
@click.option("-d", "--domain", required=True, prompt=True)
def nameservers(domain):
    """Get domain's nameservers."""
    domain = get_domain(domain)
    hostedzone = get_hosted_zone(domain)
    success_msg(
        "\n".join(record["Value"] for record in hostedzone[0]["ResourceRecords"])
    )


@domain.command("upload")
@click.option("-d", "--domain-name", required=True, prompt=True)
@click.option("-f", "--filepath", required=True, help="Enter your .zip filepath.")
def upload(domain_name, filepath):
    """Upload a zipped website file."""
    domain = get_domain(domain_name)
    resp = upload_content(domain, filepath)
    if resp:
        success_msg(f"{filepath} has been uploaded to {domain_name}")


@domain.command("remove")
@click.option("-d", "--domain-name", required=True, prompt=True)
def remove(domain_name):
    """Remove website content."""
    domain = get_domain(domain_name)
    resp = delete_content(domain)
    if resp:
        success_msg(f"Content has been deleted from {domain_name}")


@domain.command("launch")
@click.option("-d", "--domain-name", required=True, prompt=True)
def launch(domain_name):
    """Launch a domain."""
    domain = get_domain(domain_name)
    launch_site(domain)
    warning_msg("launching... this may take up to a few minutes.")


@domain.command("takedown")
@click.option("-d", "--domain-name", required=True, prompt=True)
def takedown(domain_name):
    """Takedown a domain."""
    domain = get_domain(domain_name)
    takedown_site(domain)
    warning_msg("taking down... this may take up to a few minutes.")


@domain.command("categorize")
@click.option("-d", "--domain-name", required=True, prompt=True)
def categorize(domain_name):
    """Categorize a domain."""
    domain = get_domain(domain_name)
    categories = get_categories()
    category_name = click.prompt(
        "Please enter a category", type=click.Choice(categories)
    )
    resp = categorize_site(domain, category_name)
    if resp:
        success_msg(resp)


@domain.command("checkcategory")
@click.option("-d", "--domain-name", required=True, prompt=True)
def check_category(domain_name):
    """Get a domain's category."""
    domain = get_domain(domain_name=domain_name)
    proxy_category_check(domain_id=domain.get("_id"))

    if not domain.get("category_results"):
        warning_msg("This domain has not yet been categorized.")
        return

    warning_msg("Check back in a few minutes for updated results")
    success_msg(
        "\n".join(
            f"{d.get('proxy')}: {d.get('submitted_category')}"
            for d in domain.get("category_results")
        ),
    )


@domain.command("generate")
@click.option("-d", "--domain-name", required=True, prompt=True)
def generate(domain_name):
    """Generate static content from a template."""
    templates = [template.get("name") for template in get_templates()]

    template_name = click.prompt(
        "Please choose a template", type=click.Choice(templates)
    )

    domain = get_domain(domain_name=domain_name)

    post_data = {}
    for field, gen_data in template_attributes().items():
        attribute = click.prompt(field, default=gen_data)
        post_data[field] = attribute

    resp = generate_content(
        domain_id=domain.get("_id"), template_name=template_name, data=post_data
    )
    success_msg(resp["message"])
