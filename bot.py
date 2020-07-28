import discord
import os

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send(f'Hey {message.author.name}!!!')
    if message.content.startswith('hi'):
        await message.channel.send(f'Hi {message.author.name} 😁')

@client.event
async def on_member_join(member):
    await member.channel.send(f"Welcome dear {member.name} ❤")
client.run(os.environ['TOKEN'])
