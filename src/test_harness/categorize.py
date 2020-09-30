"""Categorization controller."""
# Standard Python Libraries
# mypy: ignore-errors
# flake8: noqa
# Standard Python Libraries
import os

# Third-Party Libraries
from dotenv import load_dotenv
from selenium import webdriver

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("TWO_CAPTCHA")


def categorization_manager(domain_url):
    """Categorize site with all proxies in proxies folder."""

    # Submit domain to proxy
    proxies = os.listdir("../proxies")
    for proxy in proxies:
        try:
            driver = webdriver.Chrome(executable_path="../../drivers/chromedriver")
            exec(
                open(f"../proxies/{proxy}").read(),
                {"driver": driver, "domain": domain_url, "api_key": api_key},
            )
            driver.quit()
        except Exception as err:
            driver.quit()
            print(str(err))

    # Quit WebDriver
    driver.quit()


categorization_manager("example.com")
