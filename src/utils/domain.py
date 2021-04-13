from utils import api
import os


def get_domains(params=""):
    path = "/api/domains/"
    if params:
        path = f"{path}?{params}"
    return api.get(path)


def get_domain(domain_name):
    """Return a domain."""
    return api.get(f"/api/domains/?name={domain_name}")[0]


def get_hosted_zone(domain):
    """Return a domain's hosted zone."""
    return api.get(f"/api/domain/{domain['_id']}/records/")


def post_record(
    domain: dict, record_type: str, record_name: str, ttl: int, config: dict
):
    """Create record from API."""
    data = {
        "record_type": record_type,
        "name": record_name,
        "ttl": ttl,
        "config": config,
    }
    return api.post(f"/api/domain/{domain['_id']}/records/", json=data)


def delete_record(domain: dict, record_id: str):
    """Delete record from API."""
    return api.delete(f"/api/domain/{domain['_id']}/records/?record_id={record_id}")


def update_record(domain: dict, record: dict):
    """Update record from API."""
    return api.put(
        f"/api/domain/{domain['_id']}/records/?record_id={record['record_id']}",
        json=record,
    )


def upload_content(domain: dict, filepath: str):
    with open(filepath, "rb") as zipfile:
        content = zipfile.read()
        filename = os.path.basename(filepath)
        return api.post(
            path=f"/api/domain/{domain['_id']}/content/?category={filename}",
            files={"zip": (filename, content)},
        )


def delete_content(domain: dict):
    return api.delete(f"/api/domain/{domain['_id']}/content/")


def launch_site(domain: dict):
    return api.get(f"/api/domain/{domain['id']}/launch/")


def takedown_site(domain: dict):
    return api.delete(f"/api/domain/{domain['id']}/launch/")


def categorize_site(domain: dict, category_name: str):
    return api.get(f"/api/domain/{domain['id']}/categorize/?category={category_name}")
