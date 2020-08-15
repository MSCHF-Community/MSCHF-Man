from discord.ext import commands
import jthon

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, *, arg): #it repeats what you feed it, got it?
        await ctx.send(f"{arg}")

    @commands.command()
    async def credits(self, ctx):
        config = jthon.load('./config')
        contributors = list(config.get('contributors').data)
        await ctx.send(contributors)

def setup(bot):
    bot.add_cog(General(bot))
