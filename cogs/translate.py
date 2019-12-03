import discord
from discord.ext import commands
from googletrans import Translator

class TranslateCog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name="translate",aliases=["trans"])
    @commands.guild_only()
    async def trans(self,ctx,langs,*msg):
        src,dest = langs.split(">")
        translator = Translator()
        msg = ' '.join(msg)
        translation = translator.translate(msg, src=src, dest=dest)
        await ctx.send('`'+translation.text+'`')

def setup(bot):
	bot.add_cog(TranslateCog(bot))