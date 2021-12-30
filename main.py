from discord.ext import commands
import subprocess
TOKEN = "OTE1NzExMzk3MDQ2OTE1MDky.Yafksg.3LCmY8U935h7zezrItfYI56sOQw"

# Initialize Bot and Denote The Command Prefix
PREFIX = '!'
bot = commands.Bot(command_prefix=PREFIX)

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user: 
#         return
#     elif message.content[0] == PREFIX:
#         await message.channel.send("Willie is confused, he does not know that command...")

@bot.command()
async def run(context):
    process = subprocess.Popen(['loop.exe', 'loop.loop'],
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr and stdout:
        await context.send("```{}\n{}```".format(stderr.decode('ascii'), stdout.decode('ascii')))
    elif stderr:
        await context.send("```{}```".format(stderr.decode('ascii'))) 
    else:
        await context.send("```" + stdout.decode('ascii') + "```")
   

@bot.command()
async def Willie(context):
    await context.send("Wonka")

bot.run(TOKEN)
