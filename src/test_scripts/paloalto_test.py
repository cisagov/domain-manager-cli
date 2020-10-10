# mypy: ignore-errors
# flake8: noqa
# Standard Python Libraries
import json
import os
import sys
import time

# Third-Party Libraries
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from twocaptcha import TwoCaptcha

load_dotenv(dotenv_path="../../.env")


class TestAddurl:
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="../../drivers/chromedriver")
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_addurl(self):
        self.driver.get("https://urlfiltering.paloaltonetworks.com/")
        self.driver.set_window_size(1518, 804)
        self.driver.find_element(By.ID, "id_url").click()
        self.driver.find_element(By.ID, "id_url").send_keys("thisisreal.xyz")
        self.getAndSolve("https://urlfiltering.paloaltonetworks.com/")

        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.ID, "myLink").click()
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-plus-square").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "searchInput").click()
        self.driver.find_element(By.ID, "searchInput").send_keys("Health and Medicine")
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".cate-list-group-item:nth-child(23) > p"
        ).click()
        self.driver.find_element(By.ID, "id_comment").click()
        self.driver.find_element(By.ID, "id_comment").send_keys("Test Comment")
        self.driver.find_element(By.ID, "id_your_email").send_keys(
            "idahotester33@gmail.com"
        )
        self.driver.find_element(By.ID, "id_confirm_email").send_keys(
            "idahotester33@gmail.com"
        )
        self.getAndSolve("https://urlfiltering.paloaltonetworks.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    def getAndSolve(self, url):

        recaptcha_element = self.driver.find_element(By.CLASS_NAME, "g-recaptcha")
        sitekey = recaptcha_element.get_attribute("data-sitekey")
        print(sitekey)

        api_key = os.getenv("TWO_CAPTCHA")
        solver = TwoCaptcha(api_key)
        try:
            result = solver.recaptcha(sitekey=sitekey, url=url)

        except Exception as e:
            print(e)
        else:
            self.driver.execute_script(
                "document.getElementById('g-recaptcha-response').innerHTML='"
                + result["code"]
                + "';"
            )
            time.sleep(3)


paloalto = TestAddurl()
paloalto.setup_method()
paloalto.test_addurl()
