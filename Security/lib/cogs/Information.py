from discord.ext.commands import Cog
from discord.ext.commands import command

import discord, time, platform
from discord import __version__ as discord_version
from datetime import datetime

class Info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Info")
            self.developer = (await self.bot.application_info()).owner

    @command(name = "핑", aliases = ["ping", "latency", "delay"], help = "Bot의 핑을 확인 해보세요.")
    async def ping_command(self, ctx):
        heartbeat = round(self.bot.latency * 1000)
        
        a = round(time.time() * 1000)
        message: discord.Message = await ctx.send("🏓 **핑 확인중....**")
        b = round(time.time() * 1000)
        
        elapsed = round(b - a)
        
        embed = discord.Embed(colour = discord.Colour.red(), timestamp = datetime.utcnow())
        
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        
        embed.add_field(name = "🏓 핑 확인", 
                        value = f"Ping : {elapsed}\n"
                                f"API : {heartbeat}\n"
                                "\u200b",
                        inline = False)
        
        await message.edit(content = None, embed = embed)

    @command(name = "봇정보", aliases = ["botinfo"], help = "해당 명령어를 통해 봇의 정보를 확인해보세요.")
    async def botinfo_command(self, ctx):
        python_Version = platform.python_version()
        dpyVersion = discord.__version__
        users = len(self.bot.users)
        guilds = len(self.bot.guilds)
        
        embed = discord.Embed(colour = discord.Colour.red(),
                      timestamp = datetime.utcnow())
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        
        embed.add_field(name = f"{self.bot.user.name} - 정보 >",
                        value = f"개발자 : <:Verified_Dev:807428470115532811> <@444877320415870978>\n"
                        f"개발언어 : <:Python:848030442971463720> {python_Version}\n"
                        f"라이브러리 : <:Discord_py:848030442078470194> {dpyVersion}\n"
                        f"봇 생성일 : {self.bot.user.created_at.strftime('%Y년 %m월 %d일')} | {(datetime.utcnow() - self.bot.user.created_at).days} 일 전.\n"
                        f"봇 버전 : {self.bot.VERSION}\n"
                        f"접두사 : {self.bot.command_prefix}\n"
                        f"사용자 : {users}명 | 길드 : {guilds}개\n")
                        
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Info(bot))
