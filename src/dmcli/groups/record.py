"""CLI for managing records."""
# Third-Party Libraries
import click

# cisagov Libraries
from dmcli.utils.domain import delete_record, get_domain, post_record, update_record
from dmcli.utils.message_handling import error_msg, success_msg


@click.group()
def record():
    """Manage domain records group."""
    pass


@record.command("get")
@click.option("-d", "--domain", required=True, help="Enter a domain name", prompt=True)
def get(domain):
    """Return a domain's custom records."""
    domain = get_domain(domain)
    records = domain.get("records")
    if not records:
        error_msg("No custom records exist.")
        return

    msg = ["\n"]
    for record in records:
        msg.append(f"Id: {record['record_id']}")
        msg.append(f"Name: {record['name']}")
        msg.append(f"Type: {record['record_type']}")
        msg.append(f"TTL: {record['ttl']}")
        msg.append("Config:")

        for k, v in record["config"].items():
            msg.append(f"\t{k}: {v}")

        msg.append("\n")

    success_msg("\n".join(msg))


@record.command("add")
@click.option(
    "-d", "--domain-name", required=False, type=str, help="Domain Name", prompt=True
)
@click.option(
    "-n",
    "--record-name",
    required=True,
    type=str,
    help="Record Name",
    prompt=True,
    default="example.domain.com",
)
@click.option(
    "-t",
    "--record-type",
    type=click.Choice(
        ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SRV", "TXT", "REDIRECT"],
        case_sensitive=False,
    ),
    required=True,
    help="Record Type",
    prompt=True,
)
@click.option(
    "-l",
    "--ttl",
    required=True,
    type=int,
    default=60,
    help="TTL",
    prompt=True,
)
def add(domain_name, record_name, record_type, ttl):
    """Add record from CLI."""
    domain = get_domain(domain_name)
    config = prompt_config(record_type)
    resp = post_record(
        domain=domain,
        record_type=record_type,
        record_name=record_name,
        ttl=ttl,
        config=config,
    )
    if resp:
        success_msg("Record Successfully Added")


@record.command("delete")
@click.option("-d", "--domain-name", required=True, prompt=True)
@click.option("-i", "--record-id", required=True, prompt=True)
def delete(domain_name, record_id):
    """Delete record from CLI."""
    domain = get_domain(domain_name)
    resp = delete_record(domain=domain, record_id=record_id)
    if resp:
        success_msg("Record succesfully deleted")


@record.command("update")
@click.option("-d", "--domain-name", required=True, prompt=True)
@click.option("-i", "--record-id", required=True, prompt=True)
def update(domain_name, record_id):
    """Update record from CLI."""
    domain = get_domain(domain_name)
    record = next(
        filter(lambda x: x["record_id"] == record_id, domain.get("records", [])), None
    )
    if not record:
        error_msg("Record does not exist")
        return
    record["config"] = prompt_config(record["record_type"])
    resp = update_record(domain, record)
    if resp:
        success_msg("Record successfully updated")


def prompt_config(record_type):
    """Prompt user for record config."""
    if record_type == "REDIRECT":
        redirect_url = click.prompt("Enter domain to redirect to", type=str)
        protocol = click.prompt(
            "Enter protocol for redirects",
            type=click.Choice(["http", "https"]),
        )
        config = {"value": redirect_url, "protocol": protocol}
    else:
        lines = []
        value = click.prompt(
            f"Enter {record_type} value (Press enter for multi-line values)",
            type=str,
        )
        lines.append(value)
        while value:
            value = click.prompt(
                "Enter another line value (Leave blank to confirm)", default=""
            )
            if value:
                lines.append(value)

        if len(lines) == 1:
            config = {"value": lines[0]}
        else:
            config = {"value": "\n".join(lines)}

    return config
