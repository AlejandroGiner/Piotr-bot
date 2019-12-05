import discord
import asyncio
import time
import datetime
import os
import random
from pathlib import Path
from discord.ext import commands


class Papieska(commands.Cog):

    papTime = 74220  # Hour 20, Minute 37 UTC == 2137 CET

    def __init__(self, bot):
        self.bot = bot
        self.on = {}

    async def test(self, ctx):
        await ctx.send("pog")

    @commands.command(name="papieska")
    @commands.guild_only()
    async def papieska(self, ctx):
        await ctx.send("`PAPIESKA PROTOCOL INITIATED`")
        self.on[ctx.channel.id] = True
        while self.on[ctx.channel.id]:
            now = int(time.time())
            if (now % 86400 >= self.papTime) and (now % 86400 < self.papTime+60):
                with open(os.getcwd()+'/Desktop/bot/cogs/popepics/'+random.choice([f for f in os.listdir('Desktop/bot/cogs/popepics')]), 'rb') as f:
                    await ctx.send(content="PAPIESKA", file=discord.File(f))
            await asyncio.sleep(2)

    @commands.command(name="papieskaoff")
    @commands.guild_only()
    async def papieskaoff(self, ctx):
        await ctx.send("`PAPIESKA PROTOCOL STOPPED`")
        self.on[ctx.channel.id] = False

    @commands.command(name="papieskastate")
    @commands.guild_only()
    async def papieskastate(self, ctx):
        if self.on[ctx.channel.id]:
            s = "ACTIVE"
        else:
            s = "INACTIVE"
        await ctx.send(f"`PAPIESKA PROTOCOL IS {s}. TIME IS {(int(time.time())%3600)//60}.`")

    @commands.command(name="getpap")
    @commands.guild_only()
    async def getpap(self, ctx):
        with open(os.getcwd()+'/Desktop/bot/cogs/popepics/'+random.choice([f for f in os.listdir('Desktop/bot/cogs/popepics')]), 'rb') as f:
            await ctx.send(content="PAPIESKA", file=discord.File(f))

    @commands.command(name="papieskatime")
    async def papieskatime(self, ctx):
        papToday = datetime.datetime.combine(
            datetime.date.today(), datetime.time(21, 37))
        papTomorrow = datetime.datetime.combine(
            datetime.date.today()+datetime.timedelta(days=1), datetime.time(21, 37))
        now = datetime.datetime.now()
        diff = papToday-now
        if diff.days < 0:
            diff = papTomorrow-now

        await ctx.send(f"`Only {str(diff)[:-7]} until Papieska.`")

    @commands.command(name="papieskaSpam")
    async def papieskaspam(self, ctx):
        self.on[ctx.channel.id] = True
        while self.on[ctx.channel.id]:
            with open(os.getcwd()+'/Desktop/bot/cogs/popepics/'+random.choice([f for f in os.listdir('Desktop/bot/cogs/popepics')]), 'rb') as f:
                await ctx.send(content="PAPIESKA", file=discord.File(f))
            await asyncio.sleep(2)

    @commands.command(name="papieskaSpamOff")
    async def papieskaspamoff(self, ctx):
        self.on[ctx.channel.id] = False

    @commands.command(name="indiasuperpower")
    async def indiasuperpower(self, ctx):
        india = datetime.datetime(2020, 1, 1)
        now = datetime.datetime.now()
        countdown = india-now
        await ctx.send(f"`{countdown.days} days, {countdown.seconds//3600} hours, {(countdown.seconds%3600)//60} minutes and {countdown.seconds%60} seconds left for India to become a superpower.`"+str(discord.utils.get(ctx.guild.emojis, name="poggers")))


def setup(bot):
    bot.add_cog(Papieska(bot))
