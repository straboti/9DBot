import discord
from textanalyzer import *

token = str(open(".token","r").read()[3:])
class MyClient(discord.Client):
    async def on_ready(self):
        print('Bejelentkezve:', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        await message.channel.send(analyze(message.content))

client = MyClient()
client.run(token)