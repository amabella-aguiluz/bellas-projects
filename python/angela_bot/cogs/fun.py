import discord
from discord.ext import commands
import random
import math

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun is online.")

    @commands.command()
    async def coinflip(self, ctx):
        coin = ['Heads', 'Tails']
        embed_coin = discord.Embed(title=":coin:", description=f"{random.choice(coin)}", color=discord.Color.random())
        await ctx.send(embed=embed_coin)

    @commands.command()
    async def roll(self, ctx: commands.Context, die:str):
        die_split = [d.strip() for d in die.split('d')]
        d_split = int(die_split[1])
        die_max = int(die[1:])
        die_ans = random.randint(1, d_split)
        if die_ans <= die_max * 0.25:
            color = 0xDC2020  # red
        elif die_ans <= die_max * 0.5:
            color = 0xEAA824  # orange
        elif die_ans <= die_max * 0.75:
            color = 0x2ecc71  # green
        else:
            color = 0x3498db  # blue
        if not (die.startswith("d")):
           invalid_startswith = discord.Embed(description="Please input \'d' in the beginning of your command.", color=discord.Color.red())
           await ctx.send(embed = invalid_startswith)
        if not (die[1:].isdigit()):
            invalid_digit = discord.Embed(description="Please type in the number value of dice.", color=discord.Color.red())
            await ctx.send(embed = invalid_digit)
        if(d_split <= 1):
            too_small = discord.Embed(description=f"Please input a number greater than 1.", color=discord.Color.red())
            await ctx.send(embed = too_small)
        else:
            die_embed = discord.Embed(title=f":game_die: Rolling dice...", description=f"d{die_ans}\nThe result is **{die_ans}.**", color = color)
            await ctx.send(embed = die_embed)

    @commands.command()
    async def choose(self, ctx: commands.Context, *, question:str):
        ch = [q.strip() for q in question.split('|')]
        #ch = question.strip().split('|')
        choice_answer = random.choice(ch)
        embed_choice = discord.Embed(description=f"I recommend you go with {choice_answer}.", color=discord.Color.random())
        await ctx.send(embed=embed_choice)

    @commands.command()
    async def rate(self, ctx:commands.Context, *, rate:str):
        rate_result = random.randint(1, 10)
        if rate_result <= 3:
            color = 0xDC2020  # red
        elif rate_result <= 6:
            color = 0xEAA824  # orange
        elif rate_result <= 8:
            color = 0x2ecc71  # green
        else:
            color = 0x3498db  # blue
        rate_embed = discord.Embed(description=f"I would rate **{rate}** a **{rate_result}/10**.", color = color)
        await ctx.send(embed = rate_embed)

    @commands.command()
    async def rankfixer(self, ctx:commands.Context, *, rate:str):
        fixer_rate = {"Grade 9":0xDC2020, "Grade 8":0xDC2020,
                       "Grade 7":0xDC2020, "Grade 6":0xeEAA824,
                       "Grade 5":0xEAA824, "Grade 4":0xEAA824,
                       "Grade 3":0x2ecc71, "Grade 2":0x2ecc71,
                       "Grade 1":0x2ecc71, "Color":0x3498db}
        fixer_rate_res = random.choice(list(fixer_rate.keys()))
        fixer_color = fixer_rate[fixer_rate_res]
        rate_embed = discord.Embed(description=f"I would consider **{rate}** to be a **{fixer_rate_res}** rank Fixer.", color= fixer_color)
        await ctx.send(embed = rate_embed)

    @commands.command()
    async def fortune(self, ctx: commands.Context, *, question:str):
        responses = {"It is certain.":0x2ecc71,
                    "It is decidedly so.":0x2ecc71,
                    "Without a doubt.":0x2ecc71,
                    "Yes - definitely.":0x2ecc71,
                    "You may rely on it.":0x2ecc71,
                    "As I see it, yes.":0x2ecc71,
                    "Most likely.":0x2ecc71,
                    "Outlook good.":0x2ecc71,
                    "Yes.":0x2ecc71,
                    "Signs point to yes.":0x2ecc71,
                    "Answer hazy, try again.":0xe67e22,
                    "Ask again later.":0xe74c3c,
                    "Better not tell you now.":0xe74c3c,
                    "Cannot predict now.":0xe74c3c,
                    "Concentrate and ask again.":0xe74c3c,
                    "Don't count on it.":0xe74c3c,
                    "My send is no.":0xe74c3c,
                    "My sources say no.":0xe74c3c,
                    "Outlook not so good.":0xe74c3c,
                    "Very doubtful.":0xe67e22,
                    "Maybe.":0xe67e22}
        fortune_answer = random.choice(list(responses.keys()))
        color = responses[fortune_answer]
        embed_fortune = discord.Embed(title=f":8ball: {(question)}", description=f"{fortune_answer} {ctx.author.mention}", color=color)
        await ctx.send(embed=embed_fortune)
    
        

async def setup(bot):
        await bot.add_cog(Fun(bot))