import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready() :
    print('The bot is online.')

@client.command()
async def hi(ctx):
    await ctx.send('Hi there')

client.run('NzcyNzczNzUzNDUyNzU3MDMz.X5_jpA.Obnzijv04zMIxtruITR-grOvWs8')
