#-----imports-----
import time as t
from optparse import OptionParser #TODO: Update to a non-deprecated module
import jthon
from discord.ext import commands
import discord.utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument('--headless')
OPTIONS.add_argument('--no-sandbox')
OPTIONS.add_argument('--disable-dev-shm-usage')
DRIVER = webdriver.Chrome(chrome_options=OPTIONS, executable_path=ChromeDriverManager().install())
CONFIG = jthon.load('config')

#Config
PARSER = OptionParser() #TODO: I'm not sure what options this parses. It claims it's not a unused variable but I'm skeptical.
#-----functions-----

def is_passchannel(ctx): #only exists to control usage
    """Checks if the channel is the password checking channel."""
    return ctx.message.channel.id == 678708790878797825

def teardown_method():
    DRIVER.quit()

def test_testloginzuck(password):
    DRIVER.get("https://zuckwatch.com/")
    t.sleep(4)
    sel_password = DRIVER.find_element_by_css_selector('#__layout > div > div > div > div > div.columns > div:nth-child(1) > div > input')
    sel_login = DRIVER.find_element_by_css_selector('#__layout > div > div > div > div > div.columns > div:nth-child(1) > div > a')
    sel_password.send_keys(password)
    sel_login.click()

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
                WebDriverWait(DRIVER, 1500).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".nuxt-progress-failed")))
            except:
                await ctx.send(discord.utils.escape_mentions("**The password is:** " + passwordtry))
            finally:
                await ctx.send(discord.utils.escape_mentions("`"+passwordtry+"`"+" is incorrect."))

#-----cog load function-----

def setup(bot):
    bot.add_cog(Zuckwatch(bot))
