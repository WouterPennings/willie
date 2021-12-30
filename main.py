import os
from discord.ext import commands
from dotenv import load_dotenv
import subprocess
import datetime

PREFIX = '!'
ENCODER = 'utf-8'
bot = commands.Bot(command_prefix=PREFIX)

def GetError(err):
    err = err.decode(ENCODER)
    if len(err) > 4000:
        return err[0:100]
    return err

async def SendLoopResult(context, stdout, stderr):
    output = GetError(stdout)
    error = GetError(stderr)
    if stderr and stdout:
        await context.send("```\n{}\n{}```".format(error, output))
    elif stderr:
        await context.send("```\n{}```".format(error)) 
    else:
        await context.send("```\n{}```".format(output))

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.command()
async def run(context, *, code):
    file = open('loop.loop', 'w')
    file.write(code)
    file.close()

    process = subprocess.Popen(['loop.exe', 'loop.loop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        stdout, stderr = process.communicate(timeout=1)
        await SendLoopResult(context, stdout, stderr)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        await SendLoopResult(context, stdout, stderr)
    
    print("Succesfully executed Loop code")

@bot.command()
async def Willie(context):
    await context.send("Wonka")

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)

