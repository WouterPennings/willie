import os
from dotenv import load_dotenv
load_dotenv()

LOOP_COMPILER = "loop.exe"
DOWNLOAD_URL = "https://cdn.looplang.org/prerelease/185_Windows_AMD64_loop_0.1.0.exe"
PREFIX = '!'
TOKEN = os.getenv('TOKEN')
ENCODER = "utf-8"