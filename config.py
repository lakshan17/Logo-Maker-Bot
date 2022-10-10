
import os  
from pyrogram.types import *


# Get it from my.telegram.org
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", " ").split())
BOT_USERNAME = os.getenv("BOT_USERNAME")
START_STRING = """
**🔮 Hello There, You Can Use Me To Create Awesome Logos...**
➤ Click /help Or The Button Below To Know How To Use Me
"""
S_STICKER = os.getenv("S_STICKER", "CAACAgIAAxkBAAEH7rFjRERwMBxId7tejR9YRM4bCxQwEgACugADMNSdEYTXxIjEUGdWHgQ")

HELP = """
**🖼 How To Use Me ?**
**To Make Logo -** `/logo Your Name`
**To Make Square Logo - ** `/logosq Your Name`
**♻️ Example:** 
`/logo Lakshan`
"""
HELP_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton("𝕮𝖑𝖔𝖒𝖘𝖊", callback_data="cloce")
                 ]]
                 )
