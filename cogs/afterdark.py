from discord.ext import commands
from cogs.util import check
import random
import discord

def is_afterdark(ctx):
    return ctx.message.guild.id == 681243283774504981

def is_catchannel(ctx): #only exists to control usage
    """Checks if the channel is cat channel in afterdark."""
    return ctx.message.channel.id == 681361617845354506

def is_eyeschannel(ctx): #only exists to control usage
    """Checks if the channel is eyes channel in afterdark."""
    return ctx.message.channel.id == 681248921250693151

#def is_adgeneral(ctx):
#    """Checks if the channel is mod general channel in afterdark."""
#    return ctx.message.channel.id == 681243283774504984

dercPics = ["sexyderc.jpeg", "derc2.png", "derc3.jpg", "derc4.jpg"]

brenPics = ["bren1.jpg", "bren2.jpg", "bren3.jpg"]

kenzPics = ["kenz1.jpg", "elbow1.jpg", "elbow2.jpg", "elbow3.jpg", "elbow4.jpg", "elbow5.jpg"]

jarrettPics = ["jarrett1.jpeg", "jarrett3.jpg", "jarrett4.jpg", "jarrett5.jpg", "jarrett6.jpg"]

catPics = ["brencat1.jpg", "brencat2.jpg", "brencat3.jpg", "brencat4.jpg", "brencat5.jpg", "jarrettcat1.jpg", "kenzcat1.jpg", "plantcat1.jpg", "plantcat2.png", "plantcat3.jpg", "plantcat4.jpg", "plantcat5.jpg", "plantcat6.jpg", "plantcat7.jpg", "gothcat.png"]

class afterdark(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.check(is_eyeschannel)
    async def hornforderc(self, ctx):
        """| Allows you to horn for Derc."""
        await ctx.send(file=discord.File(random.choice(dercPics)))

    @commands.command(hidden=True)
    @commands.check(is_eyeschannel)
    async def hornforbren(self, ctx):
        await ctx.send(file=discord.File(random.choice(brenPics)))

    @commands.command(hidden=True)
    @commands.check(is_eyeschannel)
    async def unhornforkenz(self, ctx):
        await ctx.send(file=discord.File(random.choice(kenzPics)))

    @commands.command(hidden=True)
    @commands.check(is_eyeschannel)
    async def hornforj(self, ctx):
        await ctx.send(file=discord.File(random.choice(jarrettPics)))

    @commands.command(hidden=True)
    @commands.check(is_afterdark)
    async def simpforcat(self, ctx):
        await ctx.send(file=discord.File(random.choice(catPics)))

def setup(bot):
    bot.add_cog(afterdark(bot))
