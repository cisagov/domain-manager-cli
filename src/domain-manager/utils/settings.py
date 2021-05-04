"""Domain Manager Settings."""
# Standard Python Libraries
import os

# cisagov Libraries
from groups.configure import configure, get_configuration
from utils.message_handling import warning_msg

# First get settings from env var
URL = os.environ.get("DOMAIN_MANAGER_API_URL")
API_KEY = os.environ.get("DOMAIN_MANAGER_API_KEY")

# If no env var, get settings from file
if not URL or not API_KEY:
    configuration = get_configuration()
    URL = configuration.get("api_url")
    API_KEY = configuration.get("api_key")

# If still no settings, configure settings
if not URL or not API_KEY:
    warning_msg("Environment not configured. Configuring environment.")
    configure()
    configuration = get_configuration()
    URL = configuration.get("api_url")
    API_KEY = configuration.get("api_key")

# Pass in api key for authorized access
auth = {"api_key": API_KEY}
