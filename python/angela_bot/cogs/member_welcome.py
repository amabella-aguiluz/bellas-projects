import discord
from discord.ext import commands
import easy_pil
import random

class memberWelcome(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("member_welcome is online.")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        welcome_channel = member.guild.system_channel
        welcome_png = "Angela_Meet_CG.png"
        
        bg = easy_pil.Editor(f"{welcome_png}").resize((1920, 1080))
        avatar_image = await easy_pil.load_image_async(str(member.avatar.url))
        avatar = easy_pil.Editor(avatar_image).resize((250, 250)).circle_image

        font_big = easy_pil.Font.poppins(size=90, variant="bold")
        font_small = easy_pil.Font.poppins(size=60, variant="bold")

        bg.paste(avatar, (835, 340))
        bg.ellipse((835, 340), 250, 250, outline="white", stroke_width=5)

        bg.text((960, 620), f"Welcome to Lobotomy Corporation, {member.guild.name}.", color="white", font=font_big, align="center")
        bg.text((960, 740), f"{member.name} is Nugget #{member.guild.member_count}!", color="white", font=font_small, align="center")

        file_img = discord.File(fp=bg.image_bytes, filename=welcome_png)

        await welcome_channel.send(f"Welcome to Lobotomy Corporation, {member.name}.")
        await welcome_channel.send(file=file_img)

async def setup(bot):
    await bot.add_cog(memberWelcome(bot))