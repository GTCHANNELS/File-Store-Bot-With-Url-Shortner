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

╭────[ 🔅 Anya Forger 🔅]────⍟
│
├🔸 My Name: [Anya Forger](https://t.me/{BOT_USERNAME})
│
├🔸 Channel: [UniHub Official](https://t.me/Unihubofficial)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [LordSungJinwoo](https://telegram.me/LordSungJinwoo)
𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗢𝘂𝗿 𝗪𝗼𝗿𝗸 𝗕𝘆 𝗝𝗼𝗶𝗻: [UniHub Official](https://t.me/Unihubofficial)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis Is **Anya Forger**\n\nMy Father Lord Sung Jinwoo Created Me To Share Files With You Guys.
"""
