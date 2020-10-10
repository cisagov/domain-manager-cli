"""Domain Manager Settings."""
# Standard Python Libraries
import os

# Third-Party Libraries
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
URL = os.environ.get("API_URL")
API_KEY = os.environ.get("API_KEY")

# Pass in api key for authorized access
auth = {"api_key": API_KEY}
