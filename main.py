import discord 
from discord.ext import commands
import datetime

discordToken = open("token.txt","r").read

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
client.run(discordToken)

###