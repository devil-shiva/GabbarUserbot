from telethon import TelegramClient 

import os

string = os.environ['STRING_SESSION']
api_id = os.environ['API_KEY']
api_hash = os.environ['API_HASH']
news_api = os.environ['NEWS_API']

# with TelegramClient(StringSession(), api_id, api_hash) as client:
#     session_str

client = TelegramClient(string, api_id , api_hash)
