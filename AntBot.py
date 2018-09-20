import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('------')

bot.run('NDgwMTg3Mzc0NDQ2NTc1NjQ2.DoWv6A.QkLibtsIuGUUGKtJiEzqHs7g-v4')
