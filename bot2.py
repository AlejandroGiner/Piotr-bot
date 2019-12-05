import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import random
import string


def reload_env_vars():
    a = os.getenv('EXTENSIONS').split()
    b = list(map( lambda x:int(x), os.getenv('ALLOWED_CHANNELS').split()))
    c = list(map(lambda x:int(x), os.getenv('BANNED_ACCOUNT_IDS').split()))
    d = os.getenv('WELCOME_MESSAGE')
    return a,b,c,d
    

load_dotenv()
extensions,ALLOWED_CHANNELS,BANNED_ACCOUNT_IDS,WELCOME_MESSAGE = reload_env_vars()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='>>', case_insensitive=True)

for i in extensions:
    bot.load_extension('cogs.'+i)

@bot.command(name="load",hidden=True)
@commands.is_owner()
async def loadcog(ctx,*,cog: str):
    try:
        bot.load_extension('cogs.'+cog)
    except Exception as e:
        await ctx.send(f"**`ERROR:`**{type(e).__name__} - {e}")
    else:
        await ctx.send("**`SUCCESS`**")
	
@bot.command(name="unload",hidden=True)
@commands.is_owner()
async def unloadcog(ctx,*,cog: str):
    try:
        bot.unload_extension('cogs.'+cog)
    except Exception as e:
        await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
    else:
        await ctx.send('**`SUCCESS`**')

@bot.command(name="reload",hidden=True)
@commands.is_owner()
async def reloadcog(ctx,*,cog: str):
    try:
        bot.reload_extension('cogs.'+cog)
    except Exception as e:
        await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
    else:
        await ctx.send('**`SUCCESS`**')

@bot.command(name="cogs",hidden=True)
@commands.is_owner()
async def showcogs(ctx):
    pass

@bot.command(name='echo')
async def echo(ctx, *msg):
    if len(msg) == 0:
        await ctx.send('elone myeslf')
    else:
        #await ctx.send(f'i echo {msg} of type {type(msg)}')
        a=''
        for i in msg:
            for j in i:
                if j in list(string.ascii_lowercase):
                    a += ':regional_indicator_'+j.lower()+':'
            a+="    "
        await ctx.send(a)


@bot.command(name='kys',hidden=True)
@commands.is_owner()
async def kys(ctx):
    await ctx.send(":(")
    await bot.logout()

@bot.command(name='reloadenv',hidden=True)
@commands.is_owner()
async def reloadenv(ctx):
    await ctx.send("`Reloading env...`")
    load_dotenv()
    extensions,ALLOWED_CHANNELS,BANNED_ACCOUNT_IDS,WELCOME_MESSAGE = reload_env_vars()



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You don\'t have the right role cousing')
    else:
        await ctx.send(error)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.channel.id not in ALLOWED_CHANNELS and not isinstance(message.channel,discord.DMChannel):
        return
    if 'roo' in message.content.lower():
        await message.channel.send('ROOOOOOOO')

    if discord.utils.get(message.mentions, id = 519953800610709526) != None:
        await message.channel.send(str(discord.utils.get(message.guild.emojis,name='haroldweird'))+':question: ')

    if 'npc' in message.content.lower():
        await message.channel.send(str(discord.utils.get(message.guild.emojis,name='npc')))

    if any(x in message.content.lower() for x in ['piotr','pitir','pito']):
        await message.add_reaction(str(discord.utils.get(message.guild.emojis,name='piotr')))

    if any(x in message.content.lower() for x in ['aron','nazi','spinner','hitler']):
        await message.add_reaction(str(discord.utils.get(message.guild.emojis,name='spinneroffriendship')))

    if message.author.id in BANNED_ACCOUNT_IDS:
        return

    await bot.process_commands(message)

@bot.event
async def on_ready():

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name='in swamp'))
    print(f'Successfully logged in and booted...!')
    ba = await bot.fetch_channel(406642928090611712)
    await ba.send(WELCOME_MESSAGE)

bot.run(token)
