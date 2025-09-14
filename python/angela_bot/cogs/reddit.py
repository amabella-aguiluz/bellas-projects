import discord
from discord.ext import commands
from random import choice
import asyncpraw as praw

with open("cogs/reddit.txt") as file:
    # opens token
    client = file.read()

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id="3RTa0eLJOYPrU2LznnQAxw", client_secret=client, user_agent="script:lobotomemes:v1.0 (by u/Regular_Particular92)"
)


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is ready!")

    @commands.command()
    async def lobotomeme(self, ctx: commands.Context):

        subreddit = await self.reddit.subreddit("TheOdysseyHadAPurpose")
        posts_list = []

        async for post in subreddit.hot(limit=30):
            if not post.over_18 and post.author is not None and any(post.url.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif"]):
                author_name = post.author.name 
                posts_list.append((post.url, author_name, post.title, post.selftext))
            if post.author is None:
                posts_list.append((post.url, "N/A", post.title, post.selftext))

        if posts_list:
            random_post = choice(posts_list)

            meme_embed = discord.Embed(title=f"Your meme as you request, Manager {ctx.author.name}.", description=f"{random_post[2]}", color=discord.Color.random())
            meme_embed.set_author(name=f"Created by {random_post[1]} from r/TheOdysseyHadAPurpose.", icon_url=ctx.author.avatar)
            meme_embed.set_image(url=random_post[0])
            meme_embed.set_footer(text=random_post[3] if random_post[3] else "No description provided."
                                  , icon_url=None)
            await ctx.send(embed=meme_embed)

        else:
            await ctx.send("Unable to fetch post, try again later.")

    def cog_unload(self):
        self.bot.loop.create_task(self.reddit.close())

async def setup(bot):
    await bot.add_cog(Reddit(bot))