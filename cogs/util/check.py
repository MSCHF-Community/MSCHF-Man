from discord.ext import commands
from cogs.util.errors import NotContributor
import jthon


def is_contributor():
    """Checks if the user is a contributor"""
    async def predicate(ctx):
        config = jthon.load('./config')
        contributors = list(config.get('contributor').data)
        if str(ctx.author.id) in contributors:
            return True
        else:
            raise NotContributor
    return commands.check(predicate)
