import discord
from discord.ext import commands
import json, urllib.request, socket, sys
Server = "irc.ppy.sh"
Port = 6667
token = open('key.txt')
Key = token.readlines()
Username = Key[0]
ServerPassword = Key[1]
chillrdy = int('1')
bot = commands.Bot(command_prefix='~', description='Helping us help you help us all')

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((Server, Port))
data = irc.recv(1024).decode()
print('---------------')
print(data)
irc.send(data.replace('ping', 'pong').encode())
irc.send('USER'.encode())
print(irc.recv(1024).decode())
irc.send(Username.encode())
print(irc.recv(1024).decode())
irc.send('PASS'.encode())
print(irc.recv(1024).decode())
irc.send(ServerPassword.encode())
print(irc.recv(1024).decode())
print("Connected to: BanchoIRC")


@bot.event
async def on_ready():
    print('Welcome back!')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------')
@bot.command()
async def adioni(ctx):
    irc.send('msg adioni 123'.encode())
    irc.send('msg adioni: 123'.encode())
    
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

    while chillrdy == '1':
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
