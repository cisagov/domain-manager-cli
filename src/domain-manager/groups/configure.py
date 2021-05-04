from appdirs import user_config_dir
import click
from configparser import ConfigParser


app_name = "domain-manager"
config = ConfigParser()
config_file = user_config_dir(app_name)

@click.command("configure")
def configure():
    default_config = get_configuration()
    config["DEFAULT"] = {}
    config["DEFAULT"]["api_url"] = click.prompt("Enter Domain Manager Url", type=str, default=default_config.get("api_url"))
    config["DEFAULT"]["api_key"] = click.prompt("Enter API Key", type=str, default=default_config.get("api_key"))
    with open(config_file, 'w') as f:
        config.write(f)

def get_configuration():
    config.read(config_file)
    return dict(config.defaults())
