import os
from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
    API_KEY = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    MESSAGE_DUMP = os.environ.get("MESSAGE_DUMP", None)
    USE_MESSAGE_DUMP = os.environ.get("USE_MESSAGE_DUMP", "False") == "True"
    SUDO_USERS = [int(x) for x in os.environ.get("SUDO_USERS", "").split() if x]
    SUPPORT_USERS = [int(x) for x in os.environ.get("SUPPORT_USERS", "").split() if x]
    WHITELIST_USERS = [int(x) for x in os.environ.get("WHITELIST_USERS", "").split() if x]
    WEBHOOK = os.environ.get("WEBHOOK", "False") == "True"
    URL = os.environ.get("URL", None)
    PORT = int(os.environ.get("PORT", "5000"))
    CERT_PATH = os.environ.get("CERT_PATH", None)
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    DEL_CMDS = os.environ.get("DEL_CMDS", "False") == "True"
    STRICT_GBAN = os.environ.get("STRICT_GBAN", "False") == "True"
    WORKERS = int(os.environ.get("WORKERS", "8"))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", "False") == "True"
    DONATION_LINK = os.environ.get("DONATION_LINK", None)
    BMERNU_SCUT_SRELFTI = int(os.environ.get("BMERNU_SCUT_SRELFTI", "0"))
