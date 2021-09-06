import discord 
from discord.ext import commands
import datetime

discordToken = open("token.txt","r").read

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  for n in intents["kovora"]:
    if message.content.startswith(n):
      await message.channel.send("Cél észlelve: Következő óra")

client.run(discordToken)

