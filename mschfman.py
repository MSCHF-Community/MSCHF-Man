import discord
from discord.ext import commands
import jthon
from pathlib import Path
import os

config = jthon.load('config')
TOKEN = config.get('token')


def get_prefix(bot, message):
    prefix = config.get('prefix')
    if not prefix:
        prefix = '>'
    return commands.when_mentioned_or(*prefix)(bot, message)


bot = commands.Bot(command_prefix=get_prefix) #allows you to change the bot's prefix


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title=f'Command: {ctx.command.name}', colour=discord.Colour(0xFF0000),
                    description=f"{ctx.author.name}, you are on cooldown for this command for {error.retry_after:.2f}s")
        await ctx.send(embed=embed)
        return
