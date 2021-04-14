"""Category methods for API."""
# cisagov Libraries
from utils import api


def get_categories():
    """Return all categories for proxy submission."""
    return api.get("/api/categories/")
