"""Domain Manager Settings."""
# Standard Python Libraries
import os
import sys

# Third-Party Libraries
from dotenv import load_dotenv
from utils.message_handling import warning_msg

# Load environment variables from .env file
env_path = os.path.join(os.getcwd() + "/.env")
load_dotenv(dotenv_path=env_path)

URL = os.environ.get("API_URL")
API_KEY = os.environ.get("API_KEY")


def dump_env():
    """Create a new .env file."""
    url_endpoint = input("Please provide the Domain Manager URL: ")
    api_key = input("Please provide the API Key for access: ")

    env_dump = f"API_URL={url_endpoint}\nAPI_KEY={api_key}"

    env_file = open(".env", "w+")
    env_file.write(env_dump)
    env_file.close()


if not URL:
    warning_msg("You're environment variables are not setup yet.")
    dump_env()
    sys.exit("Success.. Please try again.")

# Pass in api key for authorized access
auth = {"api_key": API_KEY}
