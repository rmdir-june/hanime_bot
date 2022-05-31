import discord
from scraper import main

client = discord.Client()


@client.event
async def on_ready():
    print('fuck')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$review https://hanime.tv'):
        url = message.content[8:]
        response = main(url)
        await message.channel.send(f'{message.author.mention}{response}')
    if message.content == '$review':
        await message.channel.send(f"{message.author.mention} valid use: $review <link>")


client.run('')
