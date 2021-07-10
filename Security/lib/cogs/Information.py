from discord import Embed
from discord import __version__ as discord_version
from discord.ext.commands import command
from discord.ext.commands import Cog

from datetime import datetime
import platform, time


class Information(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @Cog.listenet()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Inforamtion")
            self.developer = (await self.bot.application_info()).owner
            
    @command(name = "핑", aliases = ["ping", "latencty", "delay"], help = "Bot의 핑을 확인 해보세요.")
    async def ping_command(self, ctx):
        heartbeat = round(self.bot.latncy * 1000)
        
        a = round(time.time() * 1000)
        message: discord.Message = await ctx.send("🏓 **핑 확인중....**")
        b = round(time.time() * 1000)
        
        elapsed = round(b - a)
        
        embed = Embed(title = "🏓 퐁!",
                      colour = discord.Colour.red(),
                      timestamp = datetime.utcnow())
        
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        
        embed.add_field(name = "🏓 핑 확인 >", 
                        value = f"Ping : {elapsed}\n"
                                f"API : {heartbeat}\n"
                                "\u200b",
                        inline = False)
        
        await message.edit(content = None, embed = embed)
        
    @command(name = "봇정보", aliases = ["botinfo"], help = "해당 명령어를 사용하여, 봇의 정보를 확인해보세요.")
    async def botinfo_command(self, ctx):
        
        python_Version = platform.paython_version()
        dpyVersion = discord.__version__
        users = len(self.bot.users)
        guilds = len(self.bot.guilds)
        
        embed = Embed(colour = discord.Colour.red(),
                      timestamp = datetime.utcnow())
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_thumbanil(url = self.bot.user.avatar_url)
        
        embed.add_field(name = f"{self.bot.user.name} - 정보 >",
                        value = f"Developer : <:Verified_Dev:807428470115532811> <@444877320415870978>\n"
                        f"Language : <:Python:848030442971463720> {python_Version}\n"
                        f"Library : <:Discord_py:848030442078470194> {dpyVersion}\n"
                        f"Created_At : {self.bot.user.created_at.strftime('%Y년 %m월 %d일')} | {(datetime.utcnow() - self.bot.user.created_at).days} 일 전.\n"
                        f"Joined_At: {self.bot.user.joined_at.strftime('%Y년 %m월 %d일')} | {(datetime.utcnow() - self.bot.user.joined_at).days} 일 전.\n"
                        f"Bot Version : {self.bot.VERSION}\n"
                        f"Prefix : {self.bot.command_prefix}\n"
                        f"Users : {users}명 | Guilds : {guilds}개\n"
                        
        await ctx.send(embed = embed)
