#-----imports-----

from discord.ext import commands
from cogs.util import check
import pytest
import time
import csv
import requests
import pandas
import json
import pytest
import time
import json
import sys
import datetime
import selenium
import time as t
from sys import stdout
from optparse import OptionParser
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverManager().install())

#Config
parser = OptionParser()
now = datetime.datetime.now()

#-----functions-----

def is_passchannel(ctx): #only exists to control usage
    """Checks if the channel is the password checking channel."""
    return ctx.message.channel.id == 678708790878797825

def teardown_method():
    driver.quit()

def test_testloginzuck(password):
    driver.get("https://zuckwatch.com/")
    t.sleep(2)
    Sel_password = driver.find_element_by_css_selector('#__layout > div > div > div > div > div.columns > div:nth-child(1) > div > input')
    Sel_Login = driver.find_element_by_css_selector('#__layout > div > div > div > div > div.columns > div:nth-child(1) > div > a')
    Sel_password.send_keys(password)
    Sel_Login.click()

#-----class & commands-----

class Zuckwatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.check(is_passchannel)
    @commands.command(aliases=['zp'])
    async def zuckpass(self, ctx, *, passwordtry):
        """| Checks a single password against the Zuckwatch API"""
        async with ctx.typing():
            test_testloginzuck(passwordtry)
            try:
                WebDriverWait(driver, 1500).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".nuxt-progress-failed")))
            except:
                await ctx.send("**The password is:** " + passwordtry)
            finally:
                await ctx.send("`"+passwordtry+"`"+" is incorrect.")

#-----cog load function-----

def setup(bot):
    bot.add_cog(Zuckwatch(bot))
