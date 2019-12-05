import discord
import random

from discord.ext import commands

class Gun():
    def __init__(self,bullets: int = 1):
        self.totalsize=6
        self.size=6
        self.bullets=min(abs(bullets),self.size)

    def shoot(self):
        if self.bullets>0:
            result=(random.randint(1,self.size) in list(range(self.size-self.bullets+1,self.size+1)))
            self.bullets=self.bullets-int(result)
        else:
            return -1
        self.size=self.size-1
        return result
        

class RussianRoulette(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.gun=Gun()

    
    @commands.command(name="Roulette",aliases=['rr','RussianRoulette','shoot','fire'])
    @commands.guild_only()
    async def rr(self, ctx):
        result=self.gun.shoot()
        if result is True:
            await ctx.send(f"{ctx.author.display_name} shoots themself in the head.")
            if self.gun.bullets==0:
                await ctx.send("That was the last bullet in the gun.")
        elif result is False:
            await ctx.send("Nothing happens.")
        else:
            await ctx.send("The gun is empty. Nothing happens.")
        

    @commands.command(name="ReloadGun")
    @commands.guild_only()
    async def reloadgun(self,ctx,bullets: int = 1):
        self.gun=Gun(bullets)
        await ctx.send(f"Reloaded with {self.gun.bullets} bullets.")


def setup(bot):
    bot.add_cog(RussianRoulette(bot))
