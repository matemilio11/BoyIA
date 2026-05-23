import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url(url):
    res = requests.get(url)
    data = res.json()
    return data["url"]

@bot.command()
async def duck(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            duck_file_name = attachments.filename
            duck_file_url = attachments.url
            await attachments.save(f"./{duck_file_name}")
            await ctx.send(duck_file_url)
    else:
        await ctx.send("envia tu imagen de un pato :V")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("envia una imagen")

bot.run("MTUwMDE0NDA1Njk2ODI4MjIxNA.GCkb96.-Ul1_Rnz8")
