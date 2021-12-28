# bot.py
import os
import discord
import random
import requests
import time
import shutil
import numpy as np 
import urllib
import cv2
from PIL import Image
import os

from dotenv import load_dotenv
from discord.ext import commands

#Initial Bot Settings
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="#")


#Preprocessing Parameters
preprocessingType = "thresh"
adaptiveThreshMethod = cv2.ADAPTIVE_THRESH_MEAN_C
threshType = cv2.THRESH_BINARY_INV
adaptiveThreshBlockSize = 9
adaptiveThreshConstant = 2


def showImage(image):
    cv2.imshow("Image", image)
    cv2.waitKey(60000)
    cv2.destroyAllWindows()


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


#Convert the uploaded image url into an OpenCV image
def url_to_image(url):
    r = requests.get(url, stream=True)
    image = cv2.imdecode(np.frombuffer(r.raw.read(), np.uint8), cv2.IMREAD_COLOR)
    return image


#Convert image to grayscale and apply threshold
def preprocessImage(image):
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if preprocessingType == "thresh":
        grayImage = cv2.adaptiveThreshold(grayImage, 255, adaptiveThreshMethod, threshType, adaptiveThreshBlockSize, adaptiveThreshConstant)
    return grayImage


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
        image = url_to_image(url)
        showImage(image)
        preprocessedImage = preprocessImage(image)
        showImage(preprocessedImage)


bot.run(TOKEN)