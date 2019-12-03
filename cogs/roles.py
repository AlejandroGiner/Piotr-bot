import discord
from discord.ext import commands


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="getroles")
    @commands.guild_only()
    async def get_roles(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.author

        troles = member.roles[1:]
        if len(troles) == 0:
            await ctx.send('```No roles.```')
            return
        roles = ""
        for role in troles:
            role = str(role)
            roles += role+', '
        await ctx.send('```'+roles[:-2]+'```')

    @commands.command(name='fuhrer', aliases=['führer'])
    @commands.has_role('Mein Führer')
    async def fuhrer(self, ctx, *, arg):
        await ctx.send('FUHRER SAYS '+arg)

    @commands.command(name='prince')
    @commands.has_role('Prince')
    async def prince(self, ctx, *, arg):
        await ctx.send('PRINCE SAYS '+arg)

    @commands.command(name='hmm',hidden=True)
    @commands.is_owner()
    async def hmm(self,ctx):
        guy = ctx.guild.get_member(285454741868118027)
        await guy.create_dm()
        await guy.dm_channel.send('pinocheto el arbusto buenos dias')



def setup(bot):
    bot.add_cog(Roles(bot))
