import discord
from discord.ext import commands

import cards
from const import TOKEN


client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is running')


@client.command()
async def ping(ctx):
    await ctx.send('Pong')


@client.command()
async def exit(ctx):
    await client.close()


@client.command()
async def cah(ctx):
    await ctx.send(cards.playCards())



if __name__ == '__main__':
    client.run(TOKEN)
