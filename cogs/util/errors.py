from discord.ext import commands


class NotContributor(commands.CommandError):
    message = """Exception raised when the message author is not a contributor of the bot."""
    pass
