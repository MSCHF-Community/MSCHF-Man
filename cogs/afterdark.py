from discord.ext import commands
from cogs.util import check
import random
import discord

def is_afterdark(ctx):
    return ctx.message.guild.id == 681243283774504981

dercPics = ["sexyderc.jpeg", "derc2.png", "derc3.jpg"]

brenPics = ["bren1.jpg", "bren2.jpg", "bren3.jpg"]

catPics = ["brencat1.jpg", "brencat2.jpg", "brencat3.jpg", "brencat4.jpg", "brencat5.jpg", "jarrettcat1.jpg", "kenzcat1.jpg", "plantcat1.jpg", "plantcat2.png"]

def is_catchannel(ctx): #only exists to control usage
    """Checks if the channel is cat channel in afterdark."""
    return ctx.message.channel.id == 681361617845354506

def is_eyeschannel(ctx): #only exists to control usage
    """Checks if the channel is eyes channel in afterdark."""
    return ctx.message.channel.id == 681248921250693151

class afterdark(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.check(is_eyeschannel)
    async def hornforderc(self, ctx):
        """| Allows you to horn over Derc, the prettiest girl in zuckwatch."""
        await ctx.send(file=discord.File(random.choice(dercPics)))

    @commands.command(hidden=True)
    @commands.check(is_eyeschannel)
    async def hornforbren(self, ctx):
        await ctx.send(file=discord.File(random.choice(brenPics)))

    @commands.command(hidden=True)
    @commands.check(is_afterdark)
    async def simpforcat(self, ctx):
        await ctx.send(file=discord.File(random.choice(catPics)))

def setup(bot):
    bot.add_cog(afterdark(bot))
