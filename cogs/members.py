import discord
from discord.ext import commands

class MembersCog(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command()
	@commands.guild_only()
	async def joined(self,ctx,*,member: discord.Member=None):
		if not member:
			member=ctx.author
		await ctx.send(f"{member.display_name} joined on {member.joined_at}")
	
	@commands.command(name="top_role",aliases=["toprole"])
	@commands.guild_only()
	async def show_toprole(self,ctx,*,member: discord.Member=None):
		if member is None:
			member = ctx.author
		if member.top_role.name[0] is "@":
			await ctx.send(f"This user doesn't have any roles.")
		else:
			await ctx.send(f"The top role for {member.display_name} is `{member.top_role.name}`.")
			
	
	@commands.command(name="perms",aliases=["perms_for","permissions"])
	@commands.guild_only()
	async def check_permissions(self,ctx,*,member: discord.Member=None):
		if not member:
			member = ctx.author
		perms="\n".join(perm for perm, value in member.guild_permissions if value)
		embed=discord.Embed(title="Permissions for:",description=ctx.guild.name,colour=member.colour)
		embed.set_author(icon_url=member.avatar_url,name=str(member))
		embed.add_field(name="\uFEFF",value=perms)
		await ctx.send(content=None,embed=embed)

	@commands.command(name="channelperms")
	@commands.guild_only()
	async def channelperms(self,ctx,member: discord.Member=None):
		if not member:
			member = ctx.author
		perms = "\n".join(perm for perm,value in iter(ctx.channel.permissions_for(member)) if value)
		embed=discord.Embed(title="Permissions for:",description=ctx.guild.name,colour=member.colour)
		embed.set_author(icon_url=member.avatar_url,name=str(member))
		embed.add_field(name="\uFEFF",value=perms)
		await ctx.send(content=None,embed=embed)

	@commands.command(name="elecciontime")
	async def elecciontime(self,ctx):
		await ctx.send("`Only 6 months until elections.`")

def setup(bot):
	bot.add_cog(MembersCog(bot))