"""Categorization controller."""
# Standard Python Libraries
# mypy: ignore-errors
# flake8: noqa
# Standard Python Libraries
import os
import time

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
            time.sleep(3)
            driver.quit()
        except Exception as err:
            driver.quit()
            print(str(err))

    # Quit WebDriver
    driver.quit()


domain_name = input("Enter a domain name: ")
category_name = input("Enter a category: ")
categorization_manager(domain_name)
