"""Template methods for API."""
# Standard Python Libraries
import os

# cisagov Libraries
from utils import api


def get_templates():
    """Get templates."""
    return api.get("/api/templates/")


def upload_template(filepath):
    """Upload template zip file."""
    with open(filepath, "rb") as zipfile:
        content = zipfile.read()
        return api.post(
            path="/api/templates/", files={"zip": (os.path.basename(filepath), content)}
        )
