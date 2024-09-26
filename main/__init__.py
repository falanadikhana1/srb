#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("API_ID", default=14852801, cast=int)
API_HASH = config("API_HASH", default="d4cee9b844c63eb5b1bcc8e3426beb40")
BOT_TOKEN = config("BOT_TOKEN", default="5869900090:AAHj7kERrEvxwlp9QaYrg_EhmNePSd-QZqs")
SESSION = config("SESSION", default="BQDiosEAOi4HnFNXHVxe8UAdypwPRANG7OAQWyuihJRTy5wmioeI518LymEUPgrA8ctO0w4jk-lVNnCoTUgIb3cvP7iDdYYos06e97fOGx8kXv5wpPQF5c1Y_8QWGQ8Uyyy5ZwdAvCF>
FORCESUB = config("FORCESUB", default="Genetry")
AUTH = config("AUTH", default="1832139347")
SUDO_USERS = []
if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
