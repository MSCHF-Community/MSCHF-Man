import time
import json
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def setup_method():
    options = webdriver.ChromeOptions()
    options.add_argument('no-sandbox')
    options.add_argument('headless')
    global driver
    global vars
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())

def login_zuckwatch(password):
    driver.get("https://zuckwatch.com/")
    driver.find_element(By.CSS_SELECTOR, ".input").click()
    driver.find_element(By.CSS_SELECTOR, ".input").send_keys(password)
    driver.find_element(By.LINK_TEXT, "Login").click()
    WebDriverWait(driver, 2000).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".nuxt-progress-failed")))
    isPresent = len(driver.find_elements(By.CSS_SELECTOR, ".nuxt-progress-failed")) > 0
    if isPresent:
        print("Incorrect password: " + password)
    else:
        print("The password is: " + password)
        return 'Correct'

def teardown_method():
    driver.quit()

checkList = ["ante", "artsem", "bb", "bellyfeel", "blackwhite", "crimestop", "crimethink", "dayorder", "doubleplusgood", "doubleplusungood", "doublethink", "duckspeak", "facecrime", "free", "–ful", "good", "goodthink", "goodsex", "ingsoc", "joycamp", "malquoted", "Miniluv", "Minipax", "Minitrue", "Miniplenty", "oldthink", "ownlife", "plusgood", "pornosec", "prolefeed", "Recdep", "rectify", "ref", "sec", "sexcrime", "speakwrite", "telescreen", "thinkpol", "unperson", "upsub", "–wise"]

setup_method()

for item in checkList:
    login_zuckwatch(item)

teardown_method()
