from os import getcwd, path

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])
is_env = path.isfile(env_file)


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default="123"))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1344569458))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default="0"))  # if not given owner id will be msg dump :)
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="",
        ).split(None)
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="",
        ).split(None)
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default=""
        ).split(None)
    ]
    # CHROME_BIN = config("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    # CHROME_DRIVER = config("CHROME_DRIVER", default="/app/.chromedriver/bin/chromedriver")
    GENIUS_API_TOKEN = config("GENIUS_API", default=None)
    # AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API", default=None)
    DB_URI = config("DB_URI", default=None)
    DB_NAME = config("DB_NAME", default="gojo_satarou")
    BDB_URI = config("BDB_URI", default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bots_network")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_bots_network")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE", default='Asia/Kolkata')
    BOT_USERNAME = ""  # Leave it as it is
    BOT_ID = ""  # Leave it as it is
    BOT_NAME = ""  # Leave it as it is


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6759025438:AAEv_AnIdr9jEkjnRNnIAJ-CFAYvSkQoaVg"
    API_ID = 24683098  # Your APP_ID from Telegram
    API_HASH = "e4055cd239464e50e69bd73057c05dd3"  # Your APP_HASH from Telegram
    OWNER_ID = 6346273488 # Your telegram user id defult to mine
    MESSAGE_DUMP = -1002105665930  # Your Private Group ID for logs if not passed your owner id will be msg dump
    DEV_USERS = []
    SUDO_USERS = []
    WHITELIST_USERS = []
    DB_URI = "mongodb+srv://herobh123456:hasnainkk07@hasnainkk07.uqjekii.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "Hinata"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    RMBG_API = ""
    PREFIX_HANDLER = ["!", "/", "$"]
    SUPPORT_GROUP = "Raiden_Support"
    SUPPORT_CHANNEL = "Raiden_Updates"
    VERSION = "ᵇᵉᵗᵃ"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = ""
    WORKERS = 8
    # CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    # CHROME_DRIVER = "/app/.chromedriver/bin/chromedriver"
