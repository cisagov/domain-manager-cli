"""Domain Manager Settings."""
# Standard Python Libraries
import os

# cisagov Libraries
from groups.configure import get_configuration

# First get settings from env var
URL = os.environ.get("DOMAIN_MANAGER_API_URL")
API_KEY = os.environ.get("DOMAIN_MANAGER_API_KEY")

# If no env var, get settings from file
if not URL or not API_KEY:
    configuration = get_configuration()
    URL = configuration.get("api_url")
    API_KEY = configuration.get("api_key")

# Pass in api key for authorized access
auth = {"api_key": API_KEY}
