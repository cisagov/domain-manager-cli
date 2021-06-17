"""Configure CLI commands."""
# Standard Python Libraries
from configparser import ConfigParser
import re

# Third-Party Libraries
from appdirs import user_config_dir
import click

app_name = "domain-manager"
config = ConfigParser()
config_file = user_config_dir(app_name)


@click.command("configure")
def configure():
    """Configure CLI."""
    default_config = get_configuration()
    config["DEFAULT"] = {}
    config["DEFAULT"]["api_url"] = click.prompt(
        "Enter Domain Manager Url",
        type=str,
        default=default_config.get("api_url"),
        value_proc=validate_url,
    ).rstrip("/")
    config["DEFAULT"]["api_key"] = click.prompt(
        "Enter API Key", type=str, default=default_config.get("api_key")
    )
    with open(config_file, "w") as f:
        config.write(f)


def validate_url(value):
    """Validate urls."""
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    try:
        if not re.match(regex, value):
            raise ValueError(value)
    except ValueError:
        raise click.BadParameter("url not formatted correctly", param=value)
    return value


def get_configuration():
    """Get default configuration."""
    config.read(config_file)
    return dict(config.defaults())
