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
import time as t
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

#-----functions-----

def is_passchannel(ctx): #only exists to control usage
    """Checks if the channel is the password checking channel."""
    return ctx.message.channel.id == 678708790878797825

def teardown_method():
    driver.quit()

def test_testloginzuck(password):
    t.sleep(4)
    driver.get("https://zuckwatch.com/")
    driver.set_window_size(1366, 734)
    driver.find_element(By.CSS_SELECTOR, ".input").click()
    driver.find_element(By.CSS_SELECTOR, ".input").send_keys(password)
    driver.find_element(By.LINK_TEXT, "Login").click()

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
                WebDriverWait(driver, 4000).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".nuxt-progress-failed")))
            except:
                await ctx.send("**The password is:** " + passwordtry)
            finally:
                await ctx.send("`"+passwordtry+"`"+" is incorrect.")

#-----cog load function-----

def setup(bot):
    bot.add_cog(Zuckwatch(bot))
