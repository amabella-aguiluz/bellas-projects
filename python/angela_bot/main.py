import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="a!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready.")

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

@bot.command()
async def ping(ctx):
    ping_embed = discord.Embed(title="ping", description="latency", color=discord.Color.blue())
    ping_embed.add_field(name=f"{bot.user.name}'s latency.", value=f"{round(bot.latency * 1000)} ms.", inline= True)
    ping_embed.set_footer(text=f"Requested by {ctx.author.name}.", icon_url=ctx.author.avatar)
    await ctx.send(embed=ping_embed)

with open("token.txt") as file:
    token = file.read()

bot.run(token)
