from discord.ext import commands
from cogs.util import check
import random
import discord

def is_afterdark(ctx):
    return ctx.message.guild.id == 681243283774504981

def is_mschfserver(ctx):
    return ctx.message.guild.id == 671536906290331676

def is_eyeschannel(ctx): #only exists to control usage
    """Checks if the channel is eyes channel in afterdark."""
    return ctx.message.channel.id == 681248921250693151

# def is_modscategory(ctx): #For testing purposes - doesn't work
    #"""Checks if the category is mods-only in afterdark."""
    #return ctx.CategoryChannel.id == 681381577099313187

dercPics = ["derc1.jpeg", "derc2.png", "derc3.jpg", "derc4.jpg", "derc5.jpg", "derc6.jpg", "derc7.png"]

brenPics = ["bren1.jpg", "bren2.jpg", "bren3.jpg"]

plantPics = ["plant1.jpg", "plant2.jpg"]

kenzPics = ["kenz1.jpg", "elbow1.jpg", "elbow2.jpg", "elbow3.jpg", "elbow4.jpg", "elbow5.jpg"]

jarrettPics = ["jarrett1.jpeg", "jarrett3.jpg", "jarrett4.jpg", "jarrett5.jpg", "jarrett6.jpg", "jarrett7.jpg", "jarrett8.jpg", "jarrett9.jpg", "jarrett10.jpeg"]

catPics = ["brencat1.jpg", "brencat2.jpg", "brencat3.jpg", "brencat4.jpg", "brencat5.jpg", "jarrettcat1.jpg", "kenzcat1.jpg", "kenzcat2.jpg", "kenzcat3.png", "kenzcat4.jpg", "plantcat1.jpg", "plantcat2.png", "plantcat3.jpg", "plantcat4.jpg", "plantcat5.jpg", "plantcat6.jpg", "plantcat7.jpg", "gothcat.png"]

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
    async def elbowpicpls(self, ctx):
        await ctx.send(file=discord.File(random.choice(kenzPics)))

    @commands.command(hidden=True)
    @commands.check(is_eyeschannel)
    async def hornforj(self, ctx):
        await ctx.send(file=discord.File(random.choice(jarrettPics)))

    @commands.command(hidden=True)
    @commands.check(is_eyeschannel)
    async def hornforplant(self, ctx):
        await ctx.send(file=discord.File(random.choice(plantPics)))

    @commands.command(hidden=True)
    @commands.check(is_afterdark)
    async def simpforcat(self, ctx):
        await ctx.send(file=discord.File(random.choice(catPics)))

def setup(bot):
    bot.add_cog(afterdark(bot))
