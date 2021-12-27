# bot.py
import os
import discord
import random
import requests
import time
import shutil

from dotenv import load_dotenv
import uuid
from discord.ext import commands

#Initial Bot Settings
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="#")


#When the bot connects to a server print server and members
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(f"{bot.user} is connected to: \"{guild.name}\"\n")

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Members:\n - {members}\n")


#Basic bot command and response
@bot.command(name="test", help="This tests sending messages in response")
async def testResponse(ctx, param1: str):
    await ctx.send(f"I am a bot and I am responding to \"{param1}\"")


#Upload an image to be processed
@bot.command(name="upload", help="Upload postgame score screen")
async def uploadImage(ctx):
    try:
        url = ctx.message.attachments[0].url

    except IndexError:
        errorMessage = "ERROR: No image attached"
        print(errorMessage)
        await ctx.send(errorMessage)

    else:
        print(f"The image url is: {url}")
        r = requests.get(url, stream=True)
        imageName = "ImageUploads/valorant5v5-" + time.strftime("%Y%m%d-%H%M%S") + ".jpeg"
        with open(imageName, "wb") as outFile:
            print(f"Image being saved to: {imageName}")
            shutil.copyfileobj(r.raw, outFile)


bot.run(TOKEN)