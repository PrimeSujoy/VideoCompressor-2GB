python
import os
import time
import re

id_pattern = re.compile(r"^-?\d+$")

class Config(object):
    API_ID = os.environ.get("API_ID", "your_api_id")
    API_HASH = os.environ.get("API_HASH", "your_api_hash")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")
    DB_URL = os.environ.get("DB_URL", "your_mongodb_url")
    DB_NAME = os.environ.get("DB_NAME", "video_compressor")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get("ADMIN", "").split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
    BOT_UPTIME = time.time()
    MAX_QUEUE_SIZE = 5
