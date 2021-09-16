import discord

token = str(open(".token","r").read()[3:])
class MyClient(discord.Client):
    async def on_ready(self):
        print('Bejelentkezve:', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(token)