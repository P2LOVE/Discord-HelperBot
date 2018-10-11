import discord
from discord.ext import commands
token = open('key.txt')
Key = token.read()
bot = commands.Bot(command_prefix='#', description='Helping us help you help us all')

@bot.event
async def on_ready():
    print('---------------')
    print('Logged with')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------')
bot.run(Key)
