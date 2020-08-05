import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
import pytest
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSubmitURL():
  def setup_method(self):
    options = Options()
    options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    self.driver = webdriver.Chrome(options=options, executable_path=r"C:\src\Repos\domain_categorization\drivers\chromedriver.exe")
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_submitURL(self):
    # Test name: Submit URL
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.trustedsource.org/")
    # 2 | setWindowSize | 1920x1040 | 
    self.driver.set_window_size(1920, 1040)
    # 3 | click | name=product | 
    self.driver.find_element(By.NAME, "product").click()
    # 4 | select | name=product | label=McAfee Real-Time Database
    dropdown = self.driver.find_element(By.NAME, "product")
    dropdown.find_element(By.XPATH, "//option[. = 'McAfee Real-Time Database']").click()
    # 5 | click | name=product | 
    self.driver.find_element(By.NAME, "product").click()
    # 6 | click | name=url | 
    self.driver.find_element(By.NAME, "url").click()
    # 7 | type | name=url | https://parkwestdental.com/
    self.driver.find_element(By.NAME, "url").send_keys("https://parkwestdental.com/")
    # 8 | click | css=tr:nth-child(5) > td | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > td").click()
    # 9 | click | css=td > .button > input | 
    self.driver.find_element(By.CSS_SELECTOR, "td > .button > input").click()
    # 10 | doubleClick | css=td > .button > input | 
    element = self.driver.find_element(By.CSS_SELECTOR, "td > .button > input")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()

test = TestSubmitURL()
test.setup_method()
test.test_submitURL()
test.teardown_method()