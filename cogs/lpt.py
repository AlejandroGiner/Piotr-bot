import discord
import random
from discord.ext import commands
LPT = ("LPT: Nervous around the person you like? Sue them. They'll be forced to see in court, well dressed & in control. Let the law be your wingman", "LPT: if you're having trouble opening your beer, the seatbelt works as a bottle opener while driving",
       "LPT: want to lose weight easily? Just move to a communist country!", "LPT: this emoji is actually a real thing, apparently. You can cook it into 'emoji parmesan' or other dishes. It tastes okay. 🍆")


class LptCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def advice(self, ctx):
        await ctx.send(random.choice(LPT))


def setup(bot):
    bot.add_cog(LptCog(bot))
