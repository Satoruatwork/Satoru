import os
from dotenv import load_dotenv
 
# Loads variables from your .env file into the environment
load_dotenv()
 
 
def _get_env(key: str, default=None, required: bool = False):
    value = os.getenv(key, default)
    if required and not value:
        raise ValueError(f"Missing required environment variable: {key}")
    return value
 
 
def _get_int_env(key: str, default=None, required: bool = False):
    value = _get_env(key, default, required)
    return int(value) if value is not None else None
 
 
def _get_bool_env(key: str, default="False"):
    return _get_env(key, default).strip().lower() in ("1", "true", "yes", "on")
 
 
def _get_list_env(key: str, default=""):
    raw = _get_env(key, default) or ""
    return [item.strip() for item in raw.split(",") if item.strip()]
 
 
# ---- Telegram API credentials (from my.telegram.org) ----
API_ID = _get_int_env("API_ID", required=True)
API_HASH = _get_env("API_HASH", required=True)
 
# ---- Bot credentials (from @BotFather) ----
BOT_TOKEN = _get_env("BOT_TOKEN", required=True)
 
# ---- Assistant / userbot session (for voice chat streaming via PyTgCalls) ----
SESSION_STRING = _get_env("SESSION_STRING", required=True)
 
# ---- Owner & admin config ----
OWNER_ID = _get_int_env("OWNER_ID", required=True)
SUDO_USERS = _get_list_env("SUDO_USERS")  # comma-separated user IDs
 
# ---- Database ----
MONGO_DB_URI = _get_env("MONGO_DB_URI", required=True)
 
# ---- Logging ----
LOG_GROUP_ID = _get_int_env("LOG_GROUP_ID")
 
# ---- Support links (optional, shown in bot menus) ----
SUPPORT_CHAT = _get_env("SUPPORT_CHAT", "")
SUPPORT_CHANNEL = _get_env("SUPPORT_CHANNEL", "")
 
# ---- Playback / queue limits ----
DURATION_LIMIT_MIN = _get_int_env("DURATION_LIMIT_MIN", "120")  # max track length in minutes
 
# ---- Misc toggles ----
DEBUG = _get_bool_env("DEBUG", "False")
