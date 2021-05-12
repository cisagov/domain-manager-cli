"""External methods for API."""
# cisagov Libraries
from dmcli.utils import api


def check_category(domain_name):
    """Check external category."""
    return api.get(f"/api/categories/{domain_name}/external/")


def categorize_external(domain_name, category):
    """Categorize external domain."""
    return api.post(
        f"/api/categories/{domain_name}/external/", json={"category": category}
    )
