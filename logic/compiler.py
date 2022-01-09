import os
import requests as req

def DownloadCompiler(url, LOOP_COMPILER):
    if os.path.exists(LOOP_COMPILER):
        os.remove(LOOP_COMPILER)

    data = req.get(url, "loop.exe")
    with open(LOOP_COMPILER, 'wb') as file:
    	file.write(data.content)