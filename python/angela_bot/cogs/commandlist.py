import discord
from discord.ext import commands

class commandList(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("commands work.")

    @commands.command(name="commands")
    async def commands(self, ctx):
        commands_embed = discord.Embed(
        title="Commands",
        description="""**level:** Check current level of yourself or another user.
**lobotomeme:** Return a random post from r/TheOdysseyHadAPurpose
**coinflip:** Flip a coin to return heads or tails.
**roll:** Roll a dice.
**choose:** Let Angela decide for you.
**rate:** Let Angela rate whatever you ask her to.
**rankfixer:** Ever wondered what you would rank at as a fixer? Angela could think of it for you!
**fortune:** Look into the 8ball and ask for a fortune."""
    )
        print("help command works")
        await ctx.send(embed=commands_embed)

async def setup(bot):
    await bot.add_cog(commandList(bot))