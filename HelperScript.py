import discord
import json, urllib.request, socket, sys, time, datetime
import asyncio
from asyncio import sleep

Server = "irc.ppy.sh"
Port = 6667
rls = open('roles.txt') # 1 line = 1 role
listr = rls.readlines()
role1 = listr[0]
token = open('key.txt') # 1st Line -  IRC Username; 2nd - IRC Password; 3rd - Discord Bot Token
Key = token.readlines()
mycreator = '266419230587617292'
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
        cntx = message.content
        Player = cntx[7:] # Argument after ~check
        if (Player == 'MyHeroMismagius') or (Player == 'p2love'):
            await bot.send_message(message.channel, 'My creator always online in my heart <3')
        else:
            irc.send('WHOIS '.encode() + Player.encode() + ' \r\n'.encode())
            while True:
                r = irc.recv(4096)
                if r.decode().find('QUIT') != -1 and r != -1:
                    print(r.decode())
                    if r.decode().find(Player) and r.decode().find('End of /WHOIS list') != -1:
                        await bot.send_message(message.channel, '`' + Player + '` is online! :3')
                        break
                    else:
                        if r.decode().find(Player) and r.decode().find('No such nick/channel') != -1:
                            await bot.send_message(message.channel, '`'+ Player + '` seems like offline :(')
                            break

    
    if message.content == '~authorize':
        author = message.author
        authorid = message.author.id
        if (authorid == mycreator):
            server = bot.get_server(message.server)
            role = discord.utils.get(message.server.roles, name=(role1)) 
            await bot.add_roles(author, role)
            await bot.send_message(message.channel, 'Welcome back, senpai ♥')
        else:
            await bot.send_message(message.channel, 'You are not my senpai!')

    if message.content.startswith('~channels'):
        cntx = message.content
        Player = cntx[10:]
        await bot.send_message(message.channel, 'WIP')
bot.run(Key[2])
