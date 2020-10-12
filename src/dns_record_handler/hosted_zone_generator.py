"""Hosted Zone generator."""
# Standard Python Libraries
import argparse
import time

# Third-Party Libraries
import boto3

# NOTE You cannot created hosted zones for TLD (Top Level Domains such as .com)


def generate_hosted_zone(domain_name):
    """
    Generate a hosted zone in AWS Route53.

    Return a list of nameservers for the user specified domain
    """
    route53 = boto3.client("route53")

    # used as unique identifier generation
    # every hosted zone must have unique identifer
    unique_identifier = time.asctime()
    create_zone = route53.create_hosted_zone(
        Name=domain_name,
        CallerReference=unique_identifier,
    )

    return "".join(create_zone["DelegationSet"]["NameServers"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--domain",
        help="enter a qualified domain such as www.example.com",
        type=str,
    )
    args = parser.parse_args()
    print(generate_hosted_zone(args.domain))
