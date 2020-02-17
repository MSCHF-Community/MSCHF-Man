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
    async def repeat(self, ctx, *, arg):
        await ctx.send(f"{arg}")

    @commands.command()
    async def ping(ctx):
        await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

    @commands.command()
    async def interrogative(self, ctx, *, arg):
        """| Allows you to send a question directly to where the bot is run, you may or may not get a response."""
        print(f"Interrogative: {arg}")
        await ctx.send(input("Response: "))

def setup(bot):
    bot.add_cog(General(bot))
