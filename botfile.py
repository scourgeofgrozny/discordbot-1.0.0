import discord
import random 
TOKEN='Enter bot token here' #Paste your bot's token from Discord Dev Portal
client=discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    username=str(message.author).split('#')[0]
    user_message=str(message.content)
    channel=str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    if message.author==client.user:
        return
    elif user_message.lower()=='never gonna' or user_message.upper()=='Never gonna':
        await message.channel.send('give you up')
        return
    elif user_message.lower()=='deez nuts' or user_message.upper()=='Deez nuts':
        await message.channel.send('gottem')
        return
    elif message.channel.name=='general':
        if user_message.lower()=='hello' or user_message.upper()=='Hello':
            await message.channel.send(f'Hello, {username}')
            return
        elif user_message.lower()=='bye' or user_message.upper()=='Bye':
            await message.channel.send(f'See you later, {username}') 
            return
        elif user_message.lower()=='!random':
            response=f'{random.randrange(1000)}'
            await message.channel.send(response)
            return 
client.run(TOKEN)
