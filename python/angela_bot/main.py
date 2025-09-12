import discord
from discord.ext import commands

import os
import asyncio

bot = commands.Bot(command_prefix="a!", intents=discord.Intents.all())
# a! is prefix to all commands

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to begin the day.")
    await bot.change_presence(activity=discord.Game("Lobotomy Corporation"))

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

@bot.command(name="hi")
async def hello(ctx):
    await ctx.send(f"Welcome to Lobotomy Corporation, Manager {ctx.author.mention}.")

@bot.command()
async def ily(ctx):
    await ctx.send(f"I love you too, {ctx.author.mention} <3")

@bot.command()
async def send_embed(ctx):
    embeded_msg = discord.Embed(title="Title of Embed", description="Description of embed", color=discord.Color.blue())
    embeded_msg.set_thumbnail(url=ctx.author.avatar)
    embeded_msg.add_field(name="name of field",value="value of field",inline=False)
    embeded_msg.set_image(url=ctx.guild.icon.url if ctx.guild.icon else None)
    embeded_msg.set_footer(text="footer text", icon_url=ctx.author.avatar)
    await ctx.send(embed=embeded_msg)


