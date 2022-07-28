import discord
import os
from dotenv import load_dotenv
from utils import *

load_dotenv()
TOKEN = os.environ.get("TOKEN")
client = discord.Client()

@client.event
async def on_message(message):
    args = message.content.split(" ")

@client.event
async def on_ready():
    print("Online")
    print(f'Connected on {totalServers(client)} servers')
    print(f'Connected to {totalUsers(client)} users')

client.run(TOKEN)