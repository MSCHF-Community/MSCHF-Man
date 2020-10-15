# ticket system cog

from discord.channel import CategoryChannel
from discord.ext import commands
from discord.ext.commands import has_permissions
import discord
from discord.utils import get
import discord.abc

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="openticket")
    @has_permissions(manage_channels=True)
    async def openTicket(self,ctx):
        """Command that allows a mod to open a room."""
        guild = ctx.message.guild
        moderator_role = get(guild.roles, name="Moderators")
        category = get(guild.categories, name="Tickets")
        author = ctx.author
        authorID = author.id
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), author: discord.PermissionOverwrite(read_messages=True), moderator_role: discord.PermissionOverwrite(read_messages=True)}

        if category is None:
                category = await guild.create_category_channel("Tickets")

        channel = await guild.create_text_channel(str(authorID), category=category, overwrites=overwrites)
        
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
