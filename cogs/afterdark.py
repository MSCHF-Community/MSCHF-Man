from discord.ext import commands
from cogs.util import check
import random
import discord

def is_afterdark(ctx):
    return ctx.message.guild.id == 681243283774504981

dercPics = ["sexyderc.jpeg", "derc2.png"]

class afterdark(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.check(is_afterdark)
    async def hornforderc(self, ctx):
        """| Allows you to horn over Derc, the prettiest girl in zuckwatch."""
        await ctx.send(file=discord.File(random.choice(dercPics)))



def setup(bot):
    bot.add_cog(afterdark(bot))