"""Categorization controller."""
# Standard Python Libraries
# mypy: ignore-errors
# flake8: noqa
# Standard Python Libraries
import os

# Third-Party Libraries
from api.documents.active_site import ActiveSite
from api.documents.proxy import Proxy
from bson.son import SON
from dotenv import load_dotenv
from flask import current_app
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("TWO_CAPTCHA")


def categorization_manager(live_site_id):
    """Manage categorization of active sites."""

    is_submitted = []
    # Submit domain to proxy
    proxies = Proxy.get_all()
    for proxy in proxies:
        try:
            driver = webdriver.Chrome(executable_path="../../drivers/chromedriver")
            exec(
                proxy.get("script").decode(),
                {"driver": driver, "url": proxy.get("url"), "domain": domain_url},
            )
            driver.quit()
        except Exception as err:
            driver.quit()
            return {"error": str(err)}

    # Quit WebDriver
    driver.quit()

    # Update database
    ActiveSite.update(live_site_id=live_site_id, is_submitted=is_submitted)
    return {
        "message": f"{domain} has been successfully categorized with Bluecoat, Fortiguard and McAfee"
    }
