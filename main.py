import os
from discord.ext import commands
from dotenv import load_dotenv
import subprocess

PREFIX = '!'
bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.command()
async def run(context, *, code):
    file = open('loop.loop', 'w')
    file.write(code)
    file.close()

    process = subprocess.Popen(['loop.exe', 'loop.loop'],
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode('utf-8'))
    print(stderr.decode('utf-8'))
    if stderr and stdout:
        await context.send("```\n{}\n{}```".format(stderr.decode('utf-8'), stdout.decode('utf-8')))
    elif stderr:
        await context.send("```\n{}```".format(stderr.decode('utf-8'))) 
    else:
        await context.send("```\n{}```".format(stdout.decode('utf-8')))

    print(stdout.decode('utf-8'))
    print(stderr.decode('utf-8'))

@bot.command()
async def Willie(context):
    await context.send("Wonka")

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)