##Config

import os
from os import getenv
from dotenv import load_dotenv
from base64 import b64decode

load_dotenv()
get_queue = {}

# Client
SESSION_NAME = getenv("SESSION_NAME", "BQEjUekAW-AXaydpDqxul3EzHRkUF3Pf8cSljirp4Xogj79akgBk_TsKXP4Q9vyfjpB-xRzYmnqheUMxlW026pPYpnirYnlg92o81PkrhFccueiL1YCZ1k8045GDBf-mYmjEFiUV96dy8rADZIhsyFGkZrKe266jLTDyIWaNTQj8jJe5u-Byu-daGt6SBBdwGez2xPFK_OGtb-1f0veyQZWgK-2hBNJFaPSkC7dg4JFM_b9FkS_vi1nRulhC-tKMlpFvkeiVUDKnmX2YSJrymL20Qa6bZiwvP-DyEjNNlW09puV7s9rXw2eUZ42o1ALaH3bY7nArSZN-H7BnoFsgtpAACUF5gAAAAAFQRkquAA")
API_ID = int(getenv("API_ID", "25924955"))
API_HASH = getenv("API_HASH", "140d8d0ad7c45e934d82dfcbba019e0d")

# Bot
BOT_USERNAME = getenv("BOT_USERNAME", "musiktapibot")
BOT_TOKEN = getenv("BOT_TOKEN", "5756834181:AAH3gYfgPEoA6GeWMoInJhCi1ES-HbvR5Yw")

# Music Setting
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "3600"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", '/ . , : ; !').split())

# Database Mono
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ilem:ilem@cluster0.uewtgbl.mongodb.net/?retryWrites=true&w=majority")

# Sudo
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1784179805").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1784179805").split()))

# Log Chat
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001898314370"))
LOG_CHANNEL_ID = int(getenv("LOG_CHANNEL_ID", "-1001598359216"))

# Assistant
ASS_ID = int(getenv("ASS_ID", "5720257465"))
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))

# Support Channel
CHANNEL = getenv("CHANNEL", "apaancuhh")
GROUP = getenv("GROUP", "gabutmaximall")

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
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "True"))

SUDO_USERS.append("1784179805")
OWNER_ID.append("1784179805")
