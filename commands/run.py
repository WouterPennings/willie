import os
import subprocess

ENCODER = 'utf-8'

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
    error = stderr.decode(ENCODER)
    if stderr and stdout:
        await context.send("```Result from execution:\n\n{}\n{}```".format(error, output))
    elif stderr:
        await context.send("```Result from execution:\n\n{}```".format(error)) 
    else:
        await context.send("```Result from execution:\n\n{}```".format(output))


async def Run(context, code):
    WriteLoop('loop.loop', code)
    print(os. getcwd())
    process = subprocess.Popen(['loop.exe', 'loop.loop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    await context.send("Willie will execute you code!")
    try:
        stdout, stderr = process.communicate(timeout=1)
        await SendLoopResult(context, stdout, stderr)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        await SendLoopResult(context, stdout, stderr)
    
    print("[INFO] Succesfully executed Loop code")