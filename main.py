﻿import discord 
from discord.ext import commands
import datetime

discordToken = open("token.txt","r").read

client = discord.Client()
intents = {
  "kovora":["Milyen óra lesz","Mi lesz a következő óra","Hol leszünk","Hol leszünk következő órán","Melyik teremben leszünk","Mi lesz a kövi óra","Hol lesz a következő óra","Melyik teremben lesz a következő óra","Melyik teremben lesz a kövi óra","Hol vagyunk"]
}
órák = [
    #hétfő:
    [
        #Órák: 
        #1:
        {
            "default":{"csop":"mono","ora":"Föci","terem":"Matek"}
        },
        {
            "default":{"csop":"szakok"},
            "csop1":{"ora":"Kémia","terem":"Labor1"},
            "csop2":{"ora":"Biosz","terem":"Finn"}
        },
        {
            "default":{"csop":"fl"},
            "fiu":{"ora":"Tesi","terem":"Kondi"},
            "lany":{"ora":"Tesi","terem":"Tornaterem"},
        },
        {
            "default":{"csop":"fl"},
            "fiu":{"ora":"Tesi","terem":"Kondi"},
            "lany":{"ora":"Tesi","terem":"Tornaterem"},
        },
        {
            "default":{"csop":"szakok"},
            "csop1":{"ora":"Biosz","terem":"Labor2"},
            "csop2":{"ora":"Lyukas"}
        },
        {
            "default":{"csop":"szakok"},
            "csop1":{"ora":"Matek","terem":"Fsz1"},
            "csop2":{"ora":"Infó","terem":"Számtech"}
        },
        {
            "default":{"csop":"mono","ora":"Magyar","terem":"Páldi"}
        },
    ],
    #kedd:
    [
        {
            "default":{"csop":"mono","ora":"Töri","terem":"Finn"}
        },
        {
            "default":{"csop":"mono","ora":"Fizika","terem":"Fizika"}#,"komm":"Sok szerencsét BB-nál! :D"}
        },
        {
            "default":{"csop":"szakok"},
            "csop1":{"ora":"Matek","terem":"Matek"},
            "csop2":{"ora":"Kémia","terem":"Labor2"}
        },
        {
            "default":{"csop":"masodikiny"},
            #ide második idegennyelv encode

        },
        {
            "default":{"csop":"angol"}
            #ide angol encode
        },
        {
            "default":{"csop":"szakok"},
            "csop1":{"ora":"Biosz","terem":"Biosz"},
            "csop2":{"ora":"Matek","terem":"Bi1"}
        },
        {
            "default":{"csop":"szakok"},
            "csop1":{"ora":"Lyukas"},
            "csop2":{"ora":"Biosz","terem":"Labor1"}
        },
    ],
    #szerda:
    [
        {
            "default":{"csop":"szakok"},
            "csop1":{"ora":"Biosz","terem":"Biosz"},
            "csop2":{"ora":"Infó","terem":"Számtech"}
        },
        {
            "default":{"csop":"angol"}
            #ide angol encode
        },
        {
                "default":{"csop":"mono","ora":"Magyar","terem":"U1"}
        },
        {
            "default":{"csop":"szakok"},
            "csop1":{"ora":"Matek","terem":"Páldi"},
            "csop2":{"ora":"Biosz","terem":"Magyar"}
        },
        {
            "default":{"csop":"szakok"},
            "csop1":{"ora":"Kémia","terem":"Labor1"},
            "csop2":{"ora":"Matek","terem":"Matek"}
        },
        {
            "default":{"csop":"masodikiny"},
            #ide második idegennyelv encode

        },
        {
            "default":{"csop":"fl"},
            "fiu":{"ora":"Tesi","terem":"Udvar"},
            "lany":{"ora":"Tesi","terem":"Kondi"},
        },
        {
            "default":{"csop":"fl"},
            "fiu":{"ora":"Tesi","terem":"Udvar"},
            "lany":{"ora":"Tesi","terem":"Kondi"},
        },
    ],
    #csüt:
    [],
    #péntek:
    []
]
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  for n in intents["kovora"]:
    if message.content.startswith(n):
      await message.channel.send("Cél észlelve: Következő óra")

client.run(discordToken)

