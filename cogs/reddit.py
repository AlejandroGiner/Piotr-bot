import discord
from discord.ext import commands
import praw
import random
reddit=praw.Reddit(client_id='B4Vixpwrf3r0nw',
		client_secret='g7ivLoa81susa1aHmS6sqR_AkrY',
		user_agent='discord:438685126684311561:1.0.0 (by /u/TotallyNotTomoe)')
class RedditCog:
	def __init__(self,bot):
		self.bot=bot
	@commands.command(name="redditpic",aliases=["redpic","pic"])
	async def redditpic(self,ctx,sub: str="pics"):
		submissions=reddit.subreddit(sub).hot()
		for i in range(0,random.randint(1,10)):
			submission=next(x for x in submissions if not x.stickied)
		await ctx.send(submission.title+submission.url)
		
	@commands.command(name="redditme")
	async def printme(self,ctx):
		await ctx.send(reddit.user.me())
def setup(bot):
	bot.add_cog(RedditCog(bot))