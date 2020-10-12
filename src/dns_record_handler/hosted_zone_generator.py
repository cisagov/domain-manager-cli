"""Hosted Zone generator."""
# Standard Python Libraries
import argparse
import time

# Third-Party Libraries
import boto3

route53 = boto3.client("route53")


def list_hosted_zones(names_only=False):
    """
    List hosted zones.

    Set names_only to true if only hosted zone names are needed.
    """
    if not names_only:
        return route53.list_hosted_zones()["HostedZones"]

    return [hosted_zone.get("Name") for hosted_zone in list_hosted_zones()]


def generate_hosted_zone(domain_name):
    """
    Generate a hosted zone in AWS Route53.

    Return a list of nameservers for the user specified domain
    """
    if f"{domain_name}." in list_hosted_zones(names_only=True):
        hosted_zone_id = "".join(
            hosted_zone.get("Id")
            for hosted_zone in list_hosted_zones()
            if hosted_zone.get("Name") == f"{domain_name}."
        )
        hosted_zone = route53.get_hosted_zone(Id=hosted_zone_id)
        return "\n".join(
            nameserver for nameserver in hosted_zone["DelegationSet"]["NameServers"]
        )

    # used as unique identifier generation
    # every hosted zone must have unique identifer
    unique_identifier = time.asctime()

    hosted_zone = route53.create_hosted_zone(
        Name=domain_name,
        CallerReference=unique_identifier,
    )

    return "\n".join(
        nameserver for nameserver in hosted_zone["DelegationSet"]["NameServers"]
    )


def delete_hosted_zone(domain_name):
    """Delete a hosted zone from Route53."""
    if f"{domain_name}." in list_hosted_zones(names_only=True):
        hosted_zone_id = "".join(
            hosted_zone.get("Id")
            for hosted_zone in list_hosted_zones()
            if hosted_zone.get("Name") == f"{domain_name}."
        )
        route53.delete_hosted_zone(Id=hosted_zone_id)
        return f"{domain_name} hosted zone has been deleted."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--domain",
        help="enter a qualified domain such as www.example.com to create a hosted zone",
        type=str,
    )
    parser.add_argument(
        "-rm",
        "--remove",
        action="store_true",
        help="enter a qualified domain such as www.example.com to create a hosted zone",
    )
    args = parser.parse_args()

    if args.remove:
        run = delete_hosted_zone(args.domain)
    else:
        run = generate_hosted_zone(args.domain)
    print(run)
