import discord
from discord.ext import commands
from .hangmanClass import *
		
class HangmanBot(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
		self.hang=Hangman('')
	@commands.command(name="hangmanStart")
	async def startgame(self,ctx,word: str):
		await ctx.send("Starting game...")
		self.hang = Hangman(word)
		await ctx.send(self.hang.getOutput())
		
	@commands.command(name="h")
	async def play(self,ctx,letter: str):
		self.hang.seek(letter)
		await ctx.send(self.hang.getOutput())


		
	
	
def setup(bot):
	bot.add_cog(HangmanBot(bot))