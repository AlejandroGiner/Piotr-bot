import discord
import random
from discord.ext import commands
class SimpleCog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command(name="tothpest")
    async def tothpest(self,ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/417045763105751070/417648270823653377/aquayes.gif")

    @commands.command(name="pog")
    async def pog(self,ctx):
        await ctx.send("POG!"+str(discord.utils.get(ctx.guild.emojis,name="poggers")))
    @commands.command(name="embeds")
    @commands.guild_only()
    async def example_embed(self,ctx):
        embed=discord.Embed(title="Example Embed",description="This is an embed \nNice",colour=0x3399ff)
        embed.set_author(name="MysterialPy",url="http://www.4chan.org/",icon_url="https://i.imgur.com/yOozn3U.jpg")
        embed.set_image(url="https://cdn.discordapp.com/attachments/406642928090611712/439170561902379009/unknown.png")
        embed.add_field(name="Embed Visualizer",value="mmmmmmmmmmmm")
        embed.set_footer(text="Made in Python with discord.py@rewrite",icon_url="https://cdn.discordapp.com/attachments/406642928090611712/439165883630354442/0iuxlwgjwuks1mq-hymxrq2.png")
        await ctx.send(content="**A simple Embed for discord.py@rewrite in cogs.**",embed=embed)

    @commands.command(name="joinvc",aliases=['jv','ffs'])
    @commands.guild_only()
    async def joinvcffs(self,ctx,pos: int = 0):
        await discord.utils.get(ctx.guild.voice_channels,id=496758156605784090).disconnect()
        self.vc = await discord.utils.get(ctx.guild.voice_channels,position=pos).connect(timeout=2.0)
        return

    @commands.command(name="leavevc")
    @commands.guild_only()
    async def joinvc(self,ctx):
       await self.vc.disconnect()

def setup(bot):
    bot.add_cog(SimpleCog(bot))