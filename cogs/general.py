from discord.ext import commands
from cogs.util import check
import pytest
import time
import csv
import requests
import pandas
import json

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        """| Overwriting default commands? Might break a bunch of shit."""
        await ctx.send("See pinned message in this channel") 
    
    @commands.command()
    async def repeat(self, ctx, *, arg):
        await ctx.send(f"{arg}")

    @commands.command()
    async def hitormiss(self, ctx):
        """| A basic ping type command, I think you can guess what this does."""
        await ctx.send("I guess I never miss, huh?")

    @commands.command()
    async def interrogative(self, ctx, *, arg):
        """| Allows you to send a question directly to where the bot is run, you may or may not get a response."""
        print(f"Interrogative: {arg}")
        await ctx.send(input("Response: "))

    @commands.command()
    async def zuckpass(self, ctx, *, arg):
        """| Checks a single password against the Zuckwatch API"""
        response = requests.post('https://k1ozwahixa.execute-api.us-east-1.amazonaws.com/dev/password',json={'password': arg})
        if response.status_code != 400:
            await ctx.send("Your submitted password is correct.")
        else:
            await ctx.send("Your submitted password is incorrect.")

def setup(bot):
    bot.add_cog(General(bot))
