"""External methods for API."""
# cisagov Libraries
from dmcli.utils import api


def get_external_domains(domain_name: str = ""):
    """Get all external domains."""
    path = "/api/external-domains/"
    if domain_name:
        path = f"{path}?name={domain_name}"
    return api.get(path)


def create_external_domain(domain_name: str, proxy_email: str):
    """Create an external domain."""
    data = {"name": domain_name, "proxy_email": proxy_email}
    return api.post("/api/external-domains/", json=data)


def categorize_external_domain(domain_id: str, category: str):
    """Categorize an external domain."""
    return api.post(
        f"api/external-domain/{domain_id}/categorize/", json={"category": category}
    )


def get_external_domain_categories(domain_id: str):
    """Get categorization data on domain categories."""
    return api.get(f"api/external-domain/{domain_id}/categorize/")
