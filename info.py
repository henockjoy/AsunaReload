import re
from os import environ
from Script import script
from time import time

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Keep-Alive URL
KEEP_ALIVE_URL = environ.get("KEEP_ALIVE_URL", "https://watery-sabina-ftx-e29385aa.koyeb.app/")  # <-- Add this line
#hyper link
HYPER_MODE = bool(environ.get('HYPER_MODE', False))
#request fsub
REQUEST_FSUB_MODE = bool(environ.get('REQUEST_FSUB_MODE', True))
# Bot settings
BOT_START_TIME = time()
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://graph.org/file/6a73466ae370b915b7f4e-815136811909794d08.jpg https://graph.org/file/da29794cc568faefde6b8-c56f26e8b5bf3ec93e.jpg https://graph.org/file/af879b552a548a7068a2a-cb70821a84c96698e1.jpg https://graph.org/file/ce24878f785fd1ff6c2e6-75d8b8a3ba551d9818.jpg https://graph.org/file/0ec5f4e80dad1c3057a77-cd5fc648f6457dabd2.jpg https://graph.org/file/4329e5902214eb5b069f7-fc8f6d83fec6b1ad69.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1824857814').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001639145278 -1001638334867').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
DEFAULT_AUTH_CHANNELS = [int(x) for x in environ.get("AUTH_CHANNEL", "-1001263870486").split() if x.lstrip('-').isdigit()]
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Yoon")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'yukkiasuna')

# File Channel Settings
FILE_CHANNELS = [int(ch) for ch in environ.get('FILE_CHANNELS', '-1003052098698 -1002534824787 -1003048222121').split()]
FILE_CHANNEL_SENDING_MODE = is_enabled(environ.get('FILE_CHANNEL_SENDING_MODE', 'True'), True)
FILE_AUTO_DELETE_SECONDS = int(environ.get('FILE_AUTO_DELETE_SECONDS', 600))  # Default: 1 hour

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001725399753'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamYoonseri')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', 'True')), True)
IMDB = is_enabled((environ.get('IMDB', 'True')), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', 'True')), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '<blockquote><code>{file_name}</code>\n\n<code>{file_caption}</code></blockquote>\n<b>⇝ Support:</b> <a href="https://t.me/TeamYoonseri">@𝚃𝚎𝚊𝚖𝚈𝚘𝚘𝚗𝚜𝚎𝚛𝚒</a>\n<b>⇝ Updates:</b> <a href="https://t.me/FT_Channels">@𝙵𝚃_𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜</a>\n\n<blockquote>⚠️ <b>This file will be auto-deleted within 10 minutes. Save it to your Saved Messages!</b></blockquote>') 
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<code>{file_name}</code>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<u><b>{title}</b></u>\n\n‣ 𝖦𝖾𝗇𝗋𝖾𝗌: {genres}\n‣ 𝖸𝖾𝖺𝗋: {year}\n‣ 𝖱𝖺𝗍𝗂𝗇𝗀: {rating}\n‣ 𝖱𝗎𝗇𝖳𝗂𝗆𝖾: {runtime} 𝗆𝗂𝗇𝗎𝗍𝖾𝗌 \n‣ 𝖠𝖼𝗍𝗈𝗋𝗌: {cast}\n‣ 𝖣𝗂𝗋𝖾𝖼𝗍𝗈𝗋: {director}\n\n‣ 𝖯𝗅𝗈𝗍: {plot}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", 4)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
