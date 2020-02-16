from discord.ext import commands
from cogs.util import check
import pytest
import time
import csv
import requests
import pandas
import json

def is_passchannel(ctx):
    return ctx.message.channel.id == 678708790878797825


class Zuckwatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(is_passchannel)
    async def zuckpass(self, ctx, *, password):
        """| Checks a single password against the Zuckwatch API"""
        async with ctx.typing():
            response = requests.post('https://k1ozwahixa.execute-api.us-east-1.amazonaws.com/dev/password',json={'password': password})
            if response.status_code != 400:
                await ctx.send("Your submitted password is correct.")
            else:
                await ctx.send("Your submitted password is incorrect.")

def setup(bot):
    bot.add_cog(Zuckwatch(bot))
