"""Application methods to use against API."""
# cisagov Libraries
from dmcli.utils import api


def get_applications(params=""):
    """Get applications."""
    path = "/api/applications/"
    if params:
        path = f"{path}?{params}"
    return api.get(path)
