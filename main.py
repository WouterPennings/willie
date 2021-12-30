import os
from discord.ext import commands
from dotenv import load_dotenv
import subprocess

PREFIX = '!'
ENCODER = 'utf-8'
bot = commands.Bot(command_prefix=PREFIX)

def WriteLoop(filename, code):
    if not os.path.isfile(filename):
        open(filename, "x")
    file = open(filename, 'w')
    file.write(code)
    file.close()

# Messages that are too long are not allowed by the discord API
def ReadyResponseLoop(err):
    err = err.decode(ENCODER)
    if len(err) > 100:
        return err[0:100]
    return err

async def SendLoopResult(context, stdout, stderr):
    output = ReadyResponseLoop(stdout)
    error = ReadyResponseLoop(stderr)
    if stderr and stdout:
        await context.send("```Result from execution:\n\n{}\n{}```".format(error, output))
    elif stderr:
        await context.send("```Result from execution:\n\n{}```".format(error)) 
    else:
        await context.send("```Result from execution:\n\n{}```".format(output))

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.command()
async def Run(context, *, code):
    WriteLoop('loop.loop', code)

    process = subprocess.Popen(['loop.exe', 'loop.loop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    await context.send("Willie will execute you code!")
    try:
        stdout, stderr = process.communicate(timeout=1)
        await SendLoopResult(context, stdout, stderr)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        await SendLoopResult(context, stdout, stderr)
    
    print("Succesfully executed Loop code")

@bot.command()
async def Help(context):
    await context.send("Soldier Willie has two commands to perform:\n > !Source -> Returns the url of the source code of Willie\n > !Run <LOOP CODE> -> Compiles and runs Loop code. You can play with Loop.")

@bot.command()
async def Source(context):
    await context.send("Source code of Willie: https://github.com/WouterPennings/willie")

@bot.command()
async def Willie(context):
    await context.send("Wonka")

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)

