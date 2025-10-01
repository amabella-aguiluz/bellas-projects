import discord
from discord.ext import commands

class commandList(commands.cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun is online.")