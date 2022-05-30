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
    if message.content.startswith('$review'):
        sender = message.author
        url = message.content[8:]
        response = main(url)
        await message.channel.send(f'{message.author.mention}{response}')


client.run('OTgwODg5MTMxNjAzMzUzNjMw.GFw_bA.zGLEDuaVPEETqKorBjKBtvxuwUs2zfzG6KkGlA')
