import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "23273287"))
  API_HASH = os.environ.get("API_HASH", "2c8dbe9c5823a819a25201d7c2ccc3c6")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6733335777:AAHpT-H-sSf9K2475m13z2zwhkScpeaFseg")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "XAnyaForgerXBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002034409660"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "publicearn.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "a0957f2447c0bd85dc4406bdf9b461592180c635")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6930184116"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://UniqueDataBase:UniqueBoyDataBase@cluster0.vaqh4dc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002106420058")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002025279206"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f""" 

╭────[𝗨𝗻𝗶𝗛𝘂𝗯 𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹]────⍟
│
├ ◉ 𝗠𝘆 𝗡𝗮𝗺𝗲: [𝗔𝗻𝘆𝗮 𝗙𝗼𝗿𝗴𝗲𝗿](https://t.me/{BOT_USERNAME})
│
├ ◉ 𝗠𝘆 𝗖𝗵𝗮𝗻𝗻𝗲𝗹: [𝗨𝗻𝗶𝗛𝘂𝗯 𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹](https://t.me/Unihubofficial)
│
╰──────[ ♡ ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [𝗟𝗼𝗿𝗱𝗦𝘂𝗻𝗴𝗝𝗶𝗻𝘄𝗼𝗼](https://telegram.me/LordSungJinwoo)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis Is **Anya Forger**\n\nMy Father Lord Sung Jinwoo Created Me To Manage UniHub's All Files For More Information Check Below ↓
"""
