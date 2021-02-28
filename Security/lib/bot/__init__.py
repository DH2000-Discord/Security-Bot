import discord
from glob import glob
from asyncio import sleep

from discord import Intents
from discord.ext.commands import Bot as BotBase

OWNER_ID = [444877320415870978]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f" {cog} Cog 준비 완료.")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class Bot(BotBase):
    def __init__(self):
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None

        super().__init__(
            command_prefix="!",
            onwer_id=OWNER_ID,
            intents=Intents.all()
        )

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} Cog 불러오기 완료")

        print("준비 완료.")

    def run(self, version):
        self.VERSION = version

        print("시작 준비중....")
        self.setup()

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("봇 시작 중....")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("봇 연결완료.")

    async def on_disconnect(self):
        print("봇 연결 끊김.")

    async def on_ready(self):
        if not self.ready:

            while not self.cogs_ready.all_ready():
                await sleep(0.5)
            self.ready = True
            print("bot ready")

        else:
            print("bot reconnected")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

bot = Bot()