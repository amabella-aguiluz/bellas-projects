import discord
from discord import app_commands
from discord.ext import commands

import os
import asyncio

bot = commands.Bot(command_prefix="a!", intents=discord.Intents.all(), help_command=None)
# a! is prefix to all commands


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to begin the day.")
    await bot.change_presence(activity=discord.Game("Lobotomy Corporation"))
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands.")
    except Exception as e:
        print("An error with syncing application commands has occured: ", e)
@bot.tree.command(name="hello", description="says hello back to the person who ran the command")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Welcome to Lobotomy Corporation, Manager {interaction.user.mention}.")




with open("token.txt") as file:
    # opens token
    token = file.read()

async def Load():
    # loads all in cogs folder
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await Load()
        await bot.start(token)

asyncio.run(main())


# @bot.command()
# async def send_embed(ctx):
#     embeded_msg = discord.Embed(title="Title of Embed", description="Description of embed", color=discord.Color.blue())
#     embeded_msg.set_thumbnail(url=ctx.author.avatar)
#     embeded_msg.add_field(name="name of field",value="value of field",inline=False)
#     embeded_msg.set_image(url=ctx.guild.icon.url if ctx.guild.icon else None)
#     embeded_msg.set_footer(text="footer text", icon_url=ctx.author.avatar)
#     await ctx.send(embed=embeded_msg)


