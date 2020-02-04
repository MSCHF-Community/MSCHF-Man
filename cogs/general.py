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

    @check.is_contributor()
    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def example(self, ctx, *, string: str = None):
        """Example of a check for user being a contributor"""
        nums_dict = {"0": ":zero:", "1": ":one:", "2": ":two:", "3": ":three:", "4": ":four:", "5": ":five:", "6": ":six:",
                     "7": ":seven:", "8": ":eight:", "9": ":nine:", " ": "    "}
        msg = "".join(f"{nums_dict.get(char)}" if char in list(nums_dict) else f':regional_indicator_{char}:'
                      for char in string if char.isalpha() or char in list(nums_dict))
        await ctx.send(f'{msg}')


def setup(bot):
    bot.add_cog(General(bot))
