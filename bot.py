import discord
from discord.ext import commands
import azure_commands as az
import ominaisuudet
import creditals as cred

bot = commands.Bot(command_prefix='#')
canUse = True

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def test(ctx):
    await ctx.send('testin')

@bot.command()
async def restart(ctx):
    await ctx.send('Restarting')
    az.restartVM()
    await ctx.send('Restarted')

@bot.command()
async def stop(ctx):
    await ctx.send('Stopping')
    az.stopVM()
    await ctx.send('Stopped')


@bot.command()
async def start(ctx):
    await ctx.send('Starting')
    az.startVM()
    await ctx.send('Started')

@bot.command()
async def deallocate(ctx):
    await ctx.send('Dealloctin')
    az.deallocateVM()
    await ctx.send('Done')

@bot.command()
async def ng(ctx):
    await ctx.send(ominaisuudet.randomWord('ng-sanat.txt'))

@bot.command()
async def on(ctx):
    await ctx.send('Valtteri on ' + ominaisuudet.randomWord('substantiivit.txt'))

bot.run(cred.DISCORD_SECRET)