import discord
import subprocess
from mcstatus import MinecraftServer
discord.x=False
token=""
client=discord.Client()
global IsOnline 
IsOnline="Offline"
server = MinecraftServer.lookup("")
discord.y=0
discord.sam="hot chin man#4517"
discord.hus="Frostyllusion#7129"
discord.an="COOLKID16#3590"
discord.countersam=0
discord.counterhus=0
discord.counteran=0
@client.event
async def on_message(message):
    if message.author==client.user:
        return
    elif message.content.lower() == "start" and not discord.x:
        await message.channel.send("Booting Up the server using JATIN's EPIC STAMINA!")
        discord.p = subprocess.Popen(["/Users/akbalsinghbhullar/Desktop/Paper Server/Start.command"],stdin=subprocess.PIPE)
        discord.x=True
    elif message.content.lower() == "stop":
        #p = subprocess.Popen(["/Users/akbalsinghbhullar/Desktop/Paper Server/Start.command"],stdin=subprocess.PIPE)
        await message.channel.send("Weirdly JATIN's STAMINA ran out? The universe broke somehow?")
        discord.p.stdin.write(b'stop')
        print(discord.p.communicate()[0])
        x=False
    elif message.content.lower() == "status":
        try:
            ping = server.ping()
        except:
            await message.channel.send("The server is Offine. with ∞ ms ping")
            pass
        else:
            await message.channel.send("Status: • Online • Ping {0} ms".format(ping))
    elif message.content.lower() == "?":
        await message.channel.send("Hmmmmmm...I Don't Know What Happened There...Maybe I Broke?")
    elif "sorry" in message.content.lower():
        await message.channel.send("It's Okay Bud...")
    elif ":(" in message.content.lower():
        await message.channel.send("It's Okay Bud...")
    elif "hi " in message.content.lower():
        await message.channel.send("Hi! {}".format(str(message.author)[:-5]))
    elif "hello" in message.content.lower():
        await message.channel.send("Hello! {}".format(str(message.author)[:-5]))
    elif "hola" in message.content.lower():
        await message.channel.send("Hola como estas mi amor 💃💃💃, {}...".format(str(message.author)[:-5]))
    elif message.content.lower() == "boot up" and discord.x:
        await message.channel.send("Server already running...")
    elif "yay" == message.content.lower():
        await message.channel.send('Yay!')
    elif "k" == message.content.lower() and str(message.author)==discord.sam and discord.countersam<=5:
        print(discord.countersam)
        await message.channel.send("k")
        discord.countersam+=1
    elif "k" == message.content.lower() and str(message.author)==discord.hus and discord.counterhus<=5:
        await message.channel.send("k")
        discord.counterhus+=1
    elif "k" == message.content.lower() and str(message.author)==discord.an and discord.counteran<=5:
        await message.channel.send("k")
        discord.counteran+=1
    elif discord.countersam>5:
        discord.sam=message.author
        for refer in range(10):
            await discord.sam.create_dm()
            await discord.sam.dm_channel.send("u spam me i spam u, so don't ever spam me sameer... im a bot and i can spam ever")
        discord.countersam=0
        discord.sam="hot chin man#4517"
    elif discord.counterhus>5:
        discord.hus=message.author
        for refer in range(10):
            await discord.hus.create_dm()
            await discord.hus.dm_channel.send("u spam me i spam u, so don't ever spam me hussein... im a bot and i can spam ever")
        discord.hus="Frostyllusion#7129"
        discord.counterhus=0
    elif discord.counteran>5:
        discord.an=message.author
        for refer in range(10):
            await discord.an.create_dm()
            await discord.an.dm_channel.send("u spam me i spam u, so don't ever spam me anant... im a bot and i can spam ever")
        discord.an="COOLKID16#3590"
        discord.counteran=0
    elif "ok" == message.content.lower():
        await message.channel.send('ok')
    elif "u r smart" == message.content.lower():
        await message.channel.send('I know I am big brain...')
client.run(token)
#subprocess.call(["open","/Users/akbalsinghbhullar/Desktop/Kill.command"]