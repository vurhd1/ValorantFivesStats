# bot.py
import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
# client = discord.Client(intents=intents)
bot = commands.Bot(intents=intents, command_prefix='#')

# @client.event
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


# @client.event
# async def on_member_join(member):
#     guild = discord.utils.get(client.guilds, name=GUILD)

#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

#     joinMessage = f"{member.name} has joined!"
#     await guild.text_channels[0].send(joinMessage)
#     print(joinMessage)


# @client.event
# async def on_message(message):
#     #Don't respond to its own messages
#     if message.author == client.user:
#         return

#     #Respond to user
#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)

@bot.command(name='test')
async def testResponse(ctx):
    await ctx.send("I am a bot and I am responding.")


bot.run(TOKEN)
# client.run(TOKEN)