"""
This file contains the functions to send messages to the discord server.
"""

# Config
from .config import DISCORD_SECRET_KEY

# Libraries
import requests

# Discord Webhook URL
webhook_url = f"https://discord.com/api/webhooks/1217558881610498099/{DISCORD_SECRET_KEY}"

# Send a message to the discord server
def send_message( message ):
    data = { "content": message }
    response = requests.post(webhook_url, json=data)
