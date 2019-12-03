import discord
import random
from discord.ext import commands


class Crop():
    def __init__(self, name, requiredGrowth):
        self.name = name
        self.growth = 0
        self.grown = False
        self.requiredGrowth = requiredGrowth

    def grow(self):
        self.growth = min(self.growth + 1, self.requiredGrowth)
        if self.growth == self.requiredGrowth:
            self.grown = True

    def harvest(self):
        self.growth = 0
        self.grown = False


class Farm():

    validCrops = {
        'maize':5,
        'potato':3,
        'asparagus':4,
        'cabbage':2,
        }

    def __init__(self, owner,name):
        self.crops = []
        self.owner = owner
        self.name = name
        self.size = 3   #max crop capacity

    def addCrop(self,crop): #if there is room, adds a crop with valid name
        if len(self.crops) == self.size:
            raise RuntimeError('There is no room for more crops in the farm.')
        if crop not in Farm.validCrops:
            raise ValueError('The crop is not valid.')
        self.crops.append(Crop(crop,Farm.validCrops[crop]))

    def asciiFarm(self):    #returns string representation of farm, with crops and their growth progress
        textfarm = '`'
        for i in self.crops:
            textfarm += f'{i.name} : {i.growth}/{i.requiredGrowth} Growth\n'
        if textfarm == '`':
            return '`Your farm is empty.`'
        return textfarm+'`'


class FarmCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.farms = {}

    @commands.command(name="createFarm")
    async def newfarm(self, ctx):
        id = ctx.author.id
        if id in self.farms:
            await ctx.send("`You already have a farm.`")
            return

        self.farms[id] = Farm(id)
        await ctx.send(f"`{ctx.author.display_name}, you now have a farm!`")

    @commands.command(name="plant")
    async def plant(self,ctx,crop):
        if ctx.author.id not in self.farms:
            await ctx.send("`You don't have a farm.`")
            return

        try:
            self.farms[ctx.author.id].addCrop(crop)
        except ValueError as err:
            await ctx.send("`That is not a valid crop.`")
        except RuntimeError as err:
            await ctx.send("`Your farm is full!`")
        else:
            await ctx.send(f"`You have planted {crop.lower()}.`")
        
    @commands.command(name="farm")
    async def farm(self,ctx):
        if ctx.author.id not in self.farms:
            await ctx.send("`You don't have a farm.`")
            return

        await ctx.send(self.farms[ctx.author.id].asciiFarm())

def setup(bot):
    bot.add_cog(FarmCog(bot))
