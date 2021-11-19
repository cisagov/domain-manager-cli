"""External methods for API."""
# cisagov Libraries
from dmcli.utils import api


def get_external_domains():
    """Get all external domains."""
    return api.get("/api/external-domains/")
