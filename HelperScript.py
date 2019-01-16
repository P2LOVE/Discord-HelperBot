import discord
import json, urllib.request, socket, sys, time, datetime
import asyncio
from asyncio import sleep

Server = "irc.ppy.sh"
Port = 6667
token = open('key.txt') # 1st Line -  IRC Username; 2nd - IRC Password; 3rd - Discord Bot Token
Key = token.readlines()
Username = Key[0]
ServerPassword = Key[1]
Recive = None
bot = discord.Client()
print('---------------')
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Set IRC socket
irc.connect((Server, Port))
irc.send(('PASS ' + ServerPassword + '\r\n').encode()) # Read Password from key.txt
irc.send(('NICK ' + Username + '\r\n').encode()) # Same 
irc.send(('END \r\n').encode())
print("Connected to: BanchoIRC")

async def receiver():
    while True:
        r = irc.recv(4096)
        if not r.find('QUIT') != -1:
            Recive.append(r)
            break
    return Recive

@bot.event
async def on_ready():
    print('---------------')
    print('Welcome back!')
    print(bot.user.name)
    print(bot.user.id)
    print(time.ctime())
    print('---------------')

@bot.event
async def on_message(message):
    if message.content == 'notice me senpai':
        author = message.author
        authorid = message.author.id
        await bot.send_message(message.channel, '<@' + authorid + '>')

    if message.content.startswith('~check'):
        Check = None
        cntx = message.content
        Player = cntx[7:] # Argument after ~check
        if (Player == 'MyHeroMismagius') or (Player == 'p2love'):
            await bot.send_message(message.channel, 'My creator always online in my heart <3')
    

bot.run(Key[2])
