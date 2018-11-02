import discord
from discord.ext import commands
import json, urllib.request, socket, sys, time, datetime
Server = "irc.ppy.sh"
Port = 6667
token = open('key.txt') # 1st Line -  IRC Username; 2nd - IRC Password; 3rd - Discord Bot Token
Key = token.readlines()
Username = Key[0]
ServerPassword = Key[1]
chillrdy = int('1')
bot = commands.Bot(command_prefix='~', description='Helping us help you help us all')
bot.remove_command('help')
print('---------------')
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Set IRC socket
irc.connect((Server, Port))
irc.send(('PASS ' + ServerPassword + '\r\n').encode()) # Read Password from key.txt
irc.send(('NICK ' + Username + '\r\n').encode()) # Same 
irc.send(('END \r\n').encode())
print("Connected to: BanchoIRC")
data = irc.recv(2048).decode() # Welcome message
print(data)

@bot.event
async def on_ready():
    print('---------------')
    print('Welcome back!')
    print(bot.user.name)
    print(bot.user.id)
    print(time.ctime())
    print('---------------')
@bot.command(pass_context=True)
async def check(ctx):
        Msg = ctx.message.content
        if Msg.find('check') > 0 :
            Player = Msg[7:] # Argument after ~check
            print(Player)
            if Player == "MyHeroMismagius":
                await ctx.send('My creator always online in my heart <3')
            else:
                if Player ==  "p2love":
                    await ctx.send('My creator always online in my heart <3')

                else:
                    irc.send('PRIVMSG BanchoBot stats '.encode() + Player.encode() + ' \r\n'.encode())
                    Check = 0
                    while Check < 30:
                        ReciveRaw = irc.recv(100).decode()
                        if ReciveRaw.endswith(':quit'):
                            Recive = ''
                        else:
                            Recive = ReciveRaw
                        print(Recive)
                        OnlineSt = Recive.find('Idle:')
                        PlaySt = Recive.find('Playing:')
                        MpSt = Recive.find('Multiplaying:')
                        MplSt = Recive.find('Multiplayer:')
                        MapSt = Recive.find('Editing:')
                        ModSt = Recive.find('Modding:')
                        TestSt = Recive.find('Testing:')
                        AfkSt = Recive.find('Afk:')
                        SubSt = Recive.find('Submitting:')
                        if OnlineSt > -1:
                            Check = 30
                            await ctx.send(Player + ' just Online!')
                        else:
                            if PlaySt > -1 | MpSt > -1 | MplSt > -1:
                                Check = 30
                                await ctx.send(Player + ' just Playing!')
                            else:
                                if MapSt > -1 | SubSt > -1:
                                    Check = 30
                                    await ctx.send(Player + ' just Editing!')
                                else:
                                    if ModSt > -1:
                                        Check = 30
                                        await ctx.send(Player + ' just Modding!')
                                    else:
                                        if TestSt > -1:
                                            Check = 30
                                            await ctx.send(Player + ' just Testing the map!')
                                        else:
                                            if AfkSt > -1:
                                                Check = 30
                                                await ctx.send(Player + ' just AFK!')
                                            else:
                                                Check = Check + 0.1 
                                                if Check > 30 | (SubSt == 0 & TestSt == 0 & ModSt == 0 & MapSt == 0 & MpSt == 0 & MplSt == 0 & OnlineSt == 0 & PlaySt == 0 & AfkSt == 0):
                                                    await ctx.send(Player + ' Offline :(')
@bot.command()
async def chill(ctx):
    chillrdy = '1'
    
    embed = discord.Embed(title="Best Chill Mixes", description="5 chillest mixes ever", color=0xef3976)
    
    embed.add_field(name="C", value="Random SuicideShepp Chill Mix")

    embed.add_field(name="H", value="1 Hour Chill Mix")

    embed.add_field(name="I", value="2 Hour Chill Mix")
    
    embed.add_field(name="L", value="Rameses B Chill Mix")
                    
    embed.add_field(name="LL", value="Random Mix")

    await ctx.send(embed=embed)

    if chillrdy == '1':
        @bot.command()
        async def C(ctx):
            chillrdy = '0'
            await ctx.send('!!!play https://www.youtube.com/watch?v=z3PpphdrEmU')
        @bot.command()
        async def H(ctx):
            chillrdy = 0
            await ctx.send('!!!play https://www.youtube.com/watch?v=H9-feB5dWhY')
        @bot.command()
        async def I(ctx):
            chillrdy = 0
            await ctx.send('!!!play https://www.youtube.com/watch?v=fWRISvgAygU')
        @bot.command()
        async def L(ctx):
            chillrdy = 0
            await ctx.send('!!!play https://www.youtube.com/watch?v=KP_LuzXROlg')
        @bot.command()
        async def LL(ctx):
            chillrdy = 0
            await ctx.send('!!!play https://www.youtube.com/watch?v=z3PpphdrEmU')


bot.run(Key[2])
