import logging

import discord

from discord.ext import commands

log = logging.getLogger(__name__)


class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
