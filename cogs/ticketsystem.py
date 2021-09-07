# ticket system cog

from discord.channel import CategoryChannel
from discord.ext import commands
from discord.ext.commands import has_permissions
import discord
from discord.utils import get
import discord.abc

ticketnumber = 1

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="openticket")
    @has_permissions(manage_channels=True)
    async def openTicket(self,ctx):
        """Command that allows a mod to open a ticket."""
        global ticketnumber
        guild = ctx.message.guild
        moderator_role = get(guild.roles, name="Moderators")
        category = get(guild.categories, name="Tickets")
        author = ctx.author
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), author: discord.PermissionOverwrite(read_messages=True), moderator_role: discord.PermissionOverwrite(read_messages=True)}

        if category is None:
                category = await guild.create_category_channel("Tickets")

        channel = await guild.create_text_channel("Ticket "+str(ticketnumber), category=category, overwrites=overwrites)
        
        ticketnumber += 1

        await channel.send("Welcome to your Ticket, "+ ctx.message.author.mention)

    @commands.command(name="closeticket", aliases=['close'])
    @has_permissions(manage_channels=True)
    async def close_room(self, ctx):
        """Command that allows a mod to close a ticket."""
        guild = ctx.message.guild
        prcatid = get(guild.categories, name="Tickets").id
        category = ctx.message.channel.category_id
        channel = ctx.message.channel
        if category == prcatid:
            await channel.delete()
        else:
            await ctx.send("This channel is not a Ticket, cannot delete.")

    @commands.command(name="adduser")
    async def add_user(self, ctx, *, user: discord.User):
        guild = ctx.message.guild
        prcatid = get(guild.categories, name="Tickets").id
        category = ctx.message.channel.category_id
        if category == prcatid:
            await ctx.channel.set_permissions(user, read_messages=True)
        else:
            await ctx.send("This channel is not a Ticket, cannot add or remove users.")
        

    @commands.command(name="removeuser")
    async def remove_user(self, ctx, *, user: discord.User):
        guild = ctx.message.guild
        prcatid = get(guild.categories, name="Tickets").id
        category = ctx.message.channel.category_id
        if category == prcatid:
            await ctx.channel.set_permissions(user, read_messages=False)
        else:
            await ctx.send("This channel is not a Ticket, cannot add or remove users.")

def setup(bot):
    bot.add_cog(Tickets(bot))
