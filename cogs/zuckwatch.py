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
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

def is_passchannel(ctx): #only exists to control usage
    """Checks if the channel is the password checking channel."""
    return ctx.message.channel.id == 678708790878797825

def teardown_method():
    driver.quit()

def test_testloginzuck(password):
    driver.get("https://zuckwatch.com/")
    driver.set_window_size(1366, 734)
    driver.find_element(By.CSS_SELECTOR, ".input").click()
    driver.find_element(By.CSS_SELECTOR, ".input").send_keys(password)
    driver.find_element(By.LINK_TEXT, "Login").click()

class Zuckwatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def zuckpass(self, ctx, *, passwordtry): #runs a single api call of a passed string against the zuckwatch password "checker", 400 is a bad response, 200 is a good one. a blank string returns 200 for some reason, but the bot luckily won't let you pass an empty
        """| Checks a single password against the Zuckwatch API"""
        async with ctx.typing():
            test_testloginzuck(passwordtry)
            try:
                WebDriverWait(driver, 1500).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".nuxt-progress-failed")))
            except:
                await ctx.send("The password is: " + passwordtry)

            finally:
                await ctx.send("That password is incorrect.")


def setup(bot):
    bot.add_cog(Zuckwatch(bot))
