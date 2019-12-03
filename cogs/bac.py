import discord
import asyncio
import time
import os
import random
from pathlib import Path
from discord.ext import commands

class BAC():
    def __init__(self):
        self.price = 0


    def update(self):
        pass
class BACog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    
def setup(bot):
    bot.add_cog(BACog(bot))
