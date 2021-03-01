import discord

from discord.ext import commands
from discord.ext.commands import Cog

class Inforamtion(Cog):
    def __init__(self, bot):
        self.bot = bot


    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Inforamtion")
            self.developer = (await self.bot.application_info()).owner

    
def setup(bot):
    bot.add_cog(Inforamtion(bot))