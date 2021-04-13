from utils import api


def check_category(domain_name):
    return api.get(f"/api/categories/{domain_name}/external/")


def categorize_external(domain_name, category):
    return api.post(
        f"/api/categories/{domain_name}/external/", json={"category": category}
    )
