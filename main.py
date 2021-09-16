import discord
from discord.flags import MessageFlags
from textanalyzer import *

token = str(open(".token","r").read()[3:])

helpDef = discord.Embed()
helpDef.title = "zsa"
class MyClient(discord.Client):
    async def on_ready(self):
        print('Bejelentkezve:', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if str(message.content)[0] == "~":
          if message.content == "~help":
            await message.channel.send(helpDef)
        ret = analyze(message.content)
        if ret.split()[0] == "NONE":
          print(ret)
          return
        else:
          await message.channel.send(ret)
          roles = []
          for n in message.author.roles:
            if str(n)[0] == ">":
              roles.append(str(n))
          await message.channel.send(roles)
client = MyClient()
client.run(token)