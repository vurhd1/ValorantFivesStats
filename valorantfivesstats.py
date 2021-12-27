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
bot = commands.Bot(intents=intents, command_prefix='#')


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.command(name="test", help="This tests sending messages in response")
async def testResponse(ctx, param1: str):
    await ctx.send(f"I am a bot and I am responding to \"{param1}\"")


bot.run(TOKEN)