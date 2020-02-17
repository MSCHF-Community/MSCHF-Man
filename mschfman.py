import discord
from discord.ext import commands
import jthon
from pathlib import Path
import os
from cogs.util.errors import NotContributor
config = jthon.load('config')
TOKEN = str(config.get("token"))

def get_prefix(bot, message):
    prefix = config.get('prefix')
    if not prefix:
        prefix = '$'
    return commands.when_mentioned_or(*prefix)(bot, message)

bot = commands.Bot(command_prefix=get_prefix) #allows you to change the bot's prefix

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title=f'Command: {ctx.command.name}', colour=discord.Colour(0xFF0000), description=f"{ctx.author.name}, you are on cooldown for this command for {error.retry_after:.2f}s")
        await ctx.send(embed=embed)
        return

    if isinstance(error, NotContributor):
        e = discord.Embed(colour=discord.Colour(0xFF0000), description=f"{ctx.author.name}, you aren't a contributor.")
        await ctx.send(embed=e)
        return

    else:
        e = discord.Embed(colour=discord.Colour(0xFF0000), description=f"{error}")
        await ctx.send(embed=e)

@bot.check #no replying to bots
async def __before_invoke(ctx):
    if not ctx.message.author.bot:
        return True

@commands.is_owner()
@bot.command(aliases=['sp'])
async def setprefix(ctx, prefix: str=None):
    if not prefix or len(prefix) >= 3:
        await ctx.send("Please provide the prefix you would like to use between 1-2 chars.")
    else:
        config['prefix'] = prefix
        config.save()
        await ctx.send(f'Prefix updated to: {prefix}')

@bot.event # Hopefully handles DMs while bot is online
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        if str(message.author) != "MSCHF Man#1788":
            print(f'Prviate message from {message.author}: "{message.content}"')
            l = open("DMLog.txt", "a")
            l.write(f'\nPrviate message from {message.author}: "{message.content}"')
            l.close()
    await bot.process_commands(message)

@bot.event
async def on_connect():
    print("Connecting...")

def load_some_cogs():
    bot.startup_extensions = []
    path = Path('./cogs')
    for dirpath, dirnames, filenames in os.walk(path):
        if dirpath.strip('./') == str(path):
            for cog in filenames:
                if cog.endswith('.py') and not cog.startswith('_'):
                    extension = 'cogs.'+cog[:-3]
                    bot.startup_extensions.append(extension)

    if __name__ == "__main__":
        for extension in bot.startup_extensions:
            try:
                bot.load_extension(extension)
                print(f'Loaded {extension}')
            except Exception as e:
                exc = f'{type(e).__name__}: {e}'
                print(f'Failed to load extension {extension}\n{exc}')

load_some_cogs()
bot.run(TOKEN, bot=True, reconnect=True)
