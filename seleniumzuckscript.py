import pytest
import time
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
password = "password"

def teardown_method():
    driver.quit()

def test_testloginzuck():
    driver.get("https://zuckwatch.com/")
    driver.set_window_size(1366, 734)
    driver.find_element(By.CSS_SELECTOR, ".input").click()
    driver.find_element(By.CSS_SELECTOR, ".input").send_keys(password)
    driver.find_element(By.LINK_TEXT, "Login").click()

    
test_testloginzuck()
try:
    WebDriverWait(driver, 1500).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".nuxt-progress-failed")))
except:
    print("The password is: " + password)
teardown_method()
