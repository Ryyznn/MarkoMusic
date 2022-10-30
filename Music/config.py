##Config

import os
from os import getenv
from dotenv import load_dotenv
from base64 import b64decode

load_dotenv()
get_queue = {}

# Client
SESSION_NAME = getenv('SESSION_NAME', 'BQDB3K6uTx6sA-7FesorsLQha3A6Q4KHzWu9QDbQQBA6qh8OHP5_vCYl8w3ZlaElqDfBolaWkMlv3k6c_P412FvvI0PaMjARLGqzxe84f6E5nIuXwAucjH6GMU98yx3MtE0WxeGjBVv0paxEFXLB7d9zvcAJIMVMCyCBS5OkzmSvRBbjie9WHTx1Xo2zjB9ab1oaoNXLc9MeaboexyqIiwpujBxoZkGNik6T1nt-RvEKvAO1UWQz0BCbJ3UTFXyRdZJf9SrSHFQJ6TCiH9pNOHN3RNIAUEGwesxpc8nZ_Z5L-yf0Jh_Pt1IunVTb-YG96KpCmo1DSe1Obx1sQS6_XYKUeQyniAA')
API_ID = int(getenv('API_ID', '22257092'))
API_HASH = getenv('API_HASH', '45e109bc6c0121c9544045a20ff9d542')

# Bot
BOT_USERNAME = getenv("BOT_USERNAME", "ryzenmusicbot")
BOT_TOKEN = getenv('BOT_TOKEN', '5561364640:AAGkgktSUqzaQ_Fubfv6Xp0nzIoESQdiLBA')

# Music Setting
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())

# Database Mono
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://zenmusic:zenmusic@cluster0.mmzrwoy.mongodb.net/?retryWrites=true&w=majority")

# Sudo
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1209395963').split()))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1534983792').split()))

# Log Chat
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001678126928"))
LOG_CHANNEL_ID = int(getenv("LOG_CHANNEL_ID", "-1001844138965"))

# Assistant
ASS_ID = int(getenv("ASS_ID", "2030872456"))
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "9000"))

# Support Channel
CHANNEL = getenv("CHANNEL", "zarchxyz")
GROUP = getenv("GROUP", "zennsupport")

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

SUDO_USERS.append("1209395963")
OWNER_ID.append("1534983792")
