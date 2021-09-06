import discord 
from discord.ext import commands
import datetime

discordToken = open("token.txt","r").read

client = discord.Client()
intents = {
  "kovora":["Milyen óra lesz","Mi lesz a következő óra","Hol leszünk","Hol leszünk következő órán","Melyik teremben leszünk","Mi lesz a kövi óra","Hol lesz a következő óra","Melyik teremben lesz a következő óra","Melyik teremben lesz a kövi óra","Hol vagyunk"]
}

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  for n in intents["kovora"]:
    if message.content.startswith(n):
      await message.channel.send("Cél észlelve: Következő óra")

client.run(discordToken)

