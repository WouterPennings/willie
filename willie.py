# Imported projects
import os
from discord.ext import commands
from dotenv import load_dotenv
import requests

# Custom Files
import commands.source as source
import commands.willie as willie
import commands.help as whelp
import commands.run as run

PREFIX = '!'
bot = commands.Bot(command_prefix=PREFIX)

data = requests.get("https://cdn.looplang.org/prerelease/185_Windows_AMD64_loop_0.1.0.exe", "loop.exe")
with open('loop.exe', 'wb') as file:
    	file.write(data.content)

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
