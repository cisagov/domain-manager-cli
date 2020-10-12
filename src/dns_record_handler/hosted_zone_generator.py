"""Hosted Zone generator."""
# Standard Python Libraries
import argparse
import time

# Third-Party Libraries
import boto3


def generate_hosted_zone(domain_name):
    """
    Generate a hosted zone in AWS Route53.

    Return a list of nameservers for the user specified domain
    """
    route53 = boto3.client("route53")

    hosted_zone_list = route53.list_hosted_zones()["HostedZones"]

    hosted_zone_names = [hosted_zone.get("Name") for hosted_zone in hosted_zone_list]

    if f"{domain_name}." in hosted_zone_names:
        hosted_zone_id = "".join(
            hosted_zone.get("Id")
            for hosted_zone in hosted_zone_list
            if hosted_zone.get("Name") == "signalsquared.com."
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--domain",
        help="enter a qualified domain such as www.example.com to create a hosted zone",
        type=str,
    )
    args = parser.parse_args()
    print(generate_hosted_zone(args.domain))
