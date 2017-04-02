import discord
import asyncio
import time
from commands import meme_command, league_command
import auth

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Add to discord via this url:')
    print('https://discordapp.com/oauth2/authorize?&client_id=' + (auth.get_auth()['zhubot']['client_id']))
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!meme'):
        tmp = await client.send_message(message.channel, 'Finding something dank...')
        meme = meme_command.get_memes()
        await client.edit_message(tmp, meme)
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!league'):
        await client.send_message(message.channel, 'Your a fag')

try:
    client.run(auth.get_auth()['zhubot']['token'])
except:
    print("Unable to run the bot!")
    print("Is your token correct?")


