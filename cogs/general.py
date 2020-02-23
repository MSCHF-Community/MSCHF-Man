from discord.ext import commands
from cogs.util import check
import pytest
import time
import csv
import requests
import pandas
import json
import discord

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, *, arg): #it repeats what you feed it, got it?
        await ctx.send(f"{arg}")

    @commands.command()
    async def interrogative(self, ctx, *, arg): #this is a more "fun" commmand, allowing people to talk directly to where the bot is run. Don't try to reload this cog with a pending interrogative, it fucks everything up
        """| Allows you to send a question directly to where the bot is run, you may or may not get a response."""
        print(f"Interrogative: {arg}")
        await ctx.send(input("Response: "))

    @commands.command()
    async def hornforderc(self, ctx):
        """| Allows you to horn over Derc, the prettiest girl in zuckwatch."""
        await ctx.send(file=discord.File("sexyderc.jpeg"))

def setup(bot):
    bot.add_cog(General(bot))
