import discord
from discord.ext import commands
from typing import Optional
from discord import app_commands


class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._synced = False
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("anon messages work.")
        if not self._synced:
            await self.bot.tree.sync() 
            self._synced = True
            print("Slash commands synced.")


    # todo: general confession in 1 channel
    @app_commands.command(name="confess", description="Send an anonymous confession.")
    async def confess(self, inter: discord.Interaction, message: str):
        confess_embed = discord.Embed(
            title= f'Anonymous Confession:\n',
            description= f'{message}\n')
        await inter.channel.send(embed= confess_embed)
        await inter.response.send_message('Your message was successfully sent!', ephemeral=True)
        

    # todo: general confession to other's dm
        # type in message: @user, message
        # dm @user
        # send in embed: "message"

    # todo: prescripts to another user
    @app_commands.command(name="prescript", description="Send a prescript to another.")
    async def prescript(self, inter: discord.Interaction, address: str, message: str):
        # type in message: @user, message
        # embed
        p_embed = discord.Embed(
            title= f'From: The Index Prescripts\n',
            description= f'To {address}\n:{message}\n')
        await inter.channel.send(embed=p_embed)
        await inter.response.send_message('Your message was successfully sent!', ephemeral=True)
        # "to @user":
        # message

async def setup(bot):
    await bot.add_cog(Messages(bot))