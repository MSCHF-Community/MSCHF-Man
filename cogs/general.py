from discord.ext import commands
from cogs.util import check


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, *, arg):
        await ctx.send(f"{arg}")

    @commands.command()
    async def hitormiss(self, ctx):
        await ctx.send("I guess I never miss, huh?")

def setup(bot):
    bot.add_cog(General(bot))
