from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, *, arg): #it repeats what you feed it, got it?
        await ctx.send(f"{arg}")

def setup(bot):
    bot.add_cog(General(bot))
