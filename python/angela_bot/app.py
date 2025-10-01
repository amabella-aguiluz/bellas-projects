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

@bot.command()
async def ily(ctx):
    await ctx.send(f"I love you too, {ctx.author.mention} <3")

@bot.command()
async def help_commands(ctx):
    help_embed = discord.Embed(title="Commands", description=
                               "**level:** Check current level of yourself or another user.\n**lobotomeme:** Return a random post from r/TheOdysseyHadAPurpose\n**coinflip**: Flip a coin to return heads or tails.\n**roll**: Roll a dice.\n**choose**: Let Angela decide for you.\n**rate**:Let Angela rate whatever you ask her to.\n**rankfixer**: Ever wondered what you would rank at as a fixer? Angela could think of it for you!\n**fortune**: Look into the 8ball and ask for a fortune.")

    await ctx.send(embed=help_embed)

# @bot.command()
# async def send_embed(ctx):
#     embeded_msg = discord.Embed(title="Title of Embed", description="Description of embed", color=discord.Color.blue())
#     embeded_msg.set_thumbnail(url=ctx.author.avatar)
#     embeded_msg.add_field(name="name of field",value="value of field",inline=False)
#     embeded_msg.set_image(url=ctx.guild.icon.url if ctx.guild.icon else None)
#     embeded_msg.set_footer(text="footer text", icon_url=ctx.author.avatar)
#     await ctx.send(embed=embeded_msg)


