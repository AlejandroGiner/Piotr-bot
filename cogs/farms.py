import discord
import random
from discord.ext import commands,tasks
from datetime import datetime
import pickle

GROWTH_INTERVAL = 86400

class Crop():
    def __init__(self, name, requiredGrowth):
        self.name = name
        self.growth = 0
        self.grown = False
        self.requiredGrowth = requiredGrowth
        self.planted_at = datetime.now()

    def grow(self):
        if self.grown:
            return
        self.growth = min(self.growth + 1, self.requiredGrowth)
        self.grown = (self.growth == self.requiredGrowth)

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
        self.harvested_crops = {}
        
        
    def fix_args(self):
        try:
            self.harvested_crops
        except:
            self.harvested_crops = {}
            return
        if type(self.harvested_crops) is list:
        
            tmp = self.harvested_crops
            self.harvested_crops = {}
            
            for i in tmp:
                if i.name in self.harvested_crops:
                    self.harvested_crops[i.name] += 1
                else:
                    self.harvested_crops[i.name] = 1
        

    def addCrop(self,crop): #if there is room, adds a crop with valid name
        if len(self.crops) == self.size:
            raise RuntimeError('There is no room for more crops in the farm.')
        if crop not in Farm.validCrops:
            raise ValueError('The crop is not valid.')
        self.crops.append(Crop(crop,Farm.validCrops[crop]))

    def update(self):
        for crop in self.crops:
            crop.grow()
            
    def harvest(self):
        amount = len(self.crops)
        for x in self.crops:
            if x.grown:
                if x.name in self.harvested_crops:
                    self.harvested_crops[x.name] += 1
                else:
                    self.harvested_crops[x.name] = 1
                
        self.crops = [x for x in self.crops if not x.grown]
        return amount-len(self.crops)

    def asciiFarm(self):    #returns string representation of farm, with crops and their growth progress
        if len(self.crops) == 0:
            return '`Your farm is empty.`'
        textfarm = f'`{self.name}:\n'
        for i in self.crops:
            textfarm += f'{i.name} : {i.growth}/{i.requiredGrowth} Growth\n'
        return textfarm+'`'
        
    def ascii_inventory(self):
        if len(self.harvested_crops) == 0:
            return '`Your inventory is empty.`'
        text_inventory = f'`{self.name}\'s inventory:\n'
        
        for i in self.harvested_crops:
            text_inventory += f'{i}: x{self.harvested_crops[i]}\n'
        
        return text_inventory+'`'


class FarmCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        try:
            with open('farms.pickle','rb') as f:
                self.farms=pickle.load(f)
        except FileNotFoundError as e:
            self.farms = {}
        self.update_farms.start()
        
        for x in self.farms.values():
            x.fix_args()
    @commands.command(name="createFarm")
    async def newfarm(self, ctx,name):
        if len(name) > 20:
            await ctx.send("`The name is too long.`")
            return
        if ctx.author.id in self.farms:
            await ctx.send("`You already have a farm.`")
            return

        self.farms[ctx.author.id] = Farm(ctx.author.id,name)
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
    async def farm(self,ctx,member: discord.Member=None):
        if member == None:
            member = ctx.author
        if member.id not in self.farms:
            await ctx.send("`You don't have a farm.`")
            return
        await ctx.send(self.farms[member.id].asciiFarm())
        
    @commands.command(name="harvest")
    async def harvest(self,ctx):
        if ctx.author.id not in self.farms:
            await ctx.send("`You don't have a farm.`")
            return
        await ctx.send(f"`Harvested {self.farms[ctx.author.id].harvest()} crops.`")
        
    @commands.command(name="myharvest")
    async def my_harvest(self,ctx):
        if ctx.author.id not in self.farms:
            await ctx.send("`You don't have a farm.`")
            return
        await ctx.send(self.farms[ctx.author.id].ascii_inventory())
        
    @commands.command(name="crops")
    async def available_crops(self,ctx):
        crops = "`AVAILABLE CROPS:\n"
        for i in Farm.validCrops:
            crops += i + " " + str(Farm.validCrops[i]) + "\n"
        await ctx.send(crops+"`")

    @commands.command(name="renamefarm")
    async def changeFarmName(self,ctx,name,member: discord.Member=None):
        if member!=None and not await self.bot.is_owner(ctx.author):
            await ctx.send("`You can't change the name of someone else's farm.`")
            return
        if member == None:
            member = ctx.author
        if len(name) > 20:
            await ctx.send("`The name is too long.`")
            return
        if member.id not in self.farms:
            await ctx.send("`You don't have a farm.`")
            return
        self.farms[member.id].name=name
        await ctx.send(f"`Changed {member.display_name}'s farm's name to {name}.`")
   
    @tasks.loop(seconds=GROWTH_INTERVAL)
    async def update_farms(self):
        for farm in self.farms.values():
            farm.update()

    def cog_unload(self):
        with open('farms.pickle','wb') as f:
            pickle.dump(self.farms,f)
        self.update_farms.cancel()

def setup(bot):
    bot.add_cog(FarmCog(bot))
