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
    author = message.author
    authorid = message.author.id
    if message.content == 'notice me senpai':
        await bot.send_message(message.channel, '<@' + authorid + '>')

@bot.event
async def on_message(message):
    if message.content.startswith('~check'):
        Check = None
        cntx = message.content
        Player = cntx[7:] # Argument after ~check
        if (Player == 'MyHeroMismagius') or (Player == 'p2love'):
            await bot.send_message(message.channel, 'My creator always online in my heart <3')
        else:
            irc.send('PRIVMSG BanchoBot stats '.encode() + Player.encode() + ' \r\n'.encode())
            for Check in range(10):
                if not Recive:
                    break
                    loop.close()
                OnlineSt = Recive.find('Idle:')
                PlaySt = Recive.find('Playing:')
                MapSt = Recive.find('Editing:')
                ModSt = Recive.find('Modding:')
                TestSt = Recive.find('Testing:')
                AfkSt = Recive.find('Afk:')
                if OnlineSt != -1:
                    await bot.send_message(Player + ' just Online!')
                    loop.close()
                    break
                else:
                    if PlaySt != -1:
                        await bot.send_message(Player + ' just Playing!')
                        loop.close()
                        break
                    else:
                        if MapSt != -1:
                            await bot.send_message(Player + ' just Editing!')
                            loop.close()
                            break
                        else:
                            if ModSt != -1:
                                await bot.send_message(Player + ' just Modding!')
                                loop.close()
                                break
                            else:
                                if TestSt != -1:
                                    await bot.send_message(Player + ' just Testing the map!')
                                    loop.close()
                                    break
                                else:
                                    if AfkSt != -1:
                                        await bot.send_message(Player + ' just AFK!')
                                        loop.close()
                                        break
                                    else:
                                        if Check == 9 | (TestSt == 0 & ModSt == 0 & MapSt == 0 & TestSt == 0 & OnlineSt == 0 & PlaySt == 0): # double check \\ on test
                                            await bot.send_message(Player + ' Offline :(')
                                            Recive = None
                                            loop.close()
                                            break

bot.run(Key[2])
