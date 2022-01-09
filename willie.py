# Imported projects
from discord.ext import commands

# Command Files
import commands.source as source
import commands.willie as willie
import commands.help as whelp
import commands.run as run

# Extras
import logic.compiler as compiler
import constants

bot = commands.Bot(command_prefix=constants.PREFIX)

@bot.event
async def on_ready():
    print(f'[INFO] {bot.user} succesfully logged in!')     
    compiler.DownloadCompiler(constants.DOWNLOAD_URL, constants.LOOP_COMPILER)
    print("[INFO] Loop compiler has been downloaded")
    
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

bot.run(constants.TOKEN)
