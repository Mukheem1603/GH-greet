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
        await message.channel.send(f'Hey {message.author}!!!')
    if message.content.startswith('help'):
        await message.channel.send(f'Heyaa {message.author} ❤\nYou can have a look at simple stats of your GitHub profile by a simple command ✨\nThe command: $info yourGitHubusername\n\nHave fun 😁')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Heyaa {member.name} ❤\nWelcome to our channel 🎉🎊\n \nGreetings from my boss , Mukheem 👨‍💻\n You can have a look at simple stats of your GitHub profile by a simple command ✨\nThe command: $info yourGitHubusername\n\nHave fun 😁'
    )
client.run(os.environ['TOKEN'])
