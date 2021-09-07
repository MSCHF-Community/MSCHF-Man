# Import Stack
import discord
from discord.ext import commands
import jthon
import os
import discord.abc
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color(0x57F287), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

# Variable Defs
help_command = commands.DefaultHelpCommand(no_category = 'Other Commands')
config = jthon.load('config')
token = str(config.get("token")) #pulls the bot token from the hidden config file
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('!!!'),
    description = "The Official bot of the Unofficial MSCHF Discord Server",
    help_command = MyHelpCommand()
)

# Function Defs
def automatic_cog_load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

#Bot Events
@bot.event
async def on_ready():
    print("MSCHF Man is operational!")

@bot.event 
async def on_command_error(ctx, error):
    e = discord.Embed(colour=discord.Colour(0xED4245), description=f"{error}")
    await ctx.send(embed=e)

@bot.event # Hopefully handles DMs while bot is online
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        if str(message.author) != "MSCHF Man#1788":
            print(f'Private message from {message.author} at {message.created_at}: "{message.content}"') #these datetime objects are in GMT
            l = open("DMLog.txt", "a")
            l.write(f'\nPrivate message from {message.author} at {message.created_at}: "{message.content}"') #these datetime objects are in GMT
            l.close()
    await bot.process_commands(message)

@bot.check #no replying to bots
async def __before_invoke(ctx):
    if not ctx.message.author.bot:
        return True

#Bot Commands
@commands.is_owner()
@bot.command()
async def shutdown(ctx):
    """Allows the owner of the bot to shut down the bot from within Discord."""
    e = discord.Embed(colour=discord.Colour(0x57F287), description="Command Received, Shutting down MSCHF Man!")
    await ctx.send(embed=e)
    exit()

automatic_cog_load()

bot.run(token)