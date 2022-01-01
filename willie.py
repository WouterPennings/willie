# Imported projects
import os
from discord.ext import commands
from dotenv import load_dotenv

# Custom Files
import commands.source as source
import commands.willie as willie
import commands.help as whelp
import commands.run as run

PREFIX = '!'
bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.command()
async def Run(context, *, code):
    await run.Run(context, code)

@bot.command()
async def Help(context):
    await whelp.WHelp(context)

@bot.command()
async def Source(context):
    await source.Source(context)

@bot.command()
async def Willie(context):
    await willie.Willie(context)

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
