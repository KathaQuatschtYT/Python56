import logging
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(
  command_prefix=None,
  intents=discord.Intents.default(),
  activity=discord.Activity(type=discord.ActivityType.playing, named="Hello World!"),
  status=discord.Status.online,
  sync_commands=False,
  delete_not_existing_commands=False
)

if __name__ == '__main__':
  log.info("Starting bot...")
  token = os.getenv('BOT_TOKEN')
  bot.run(token)
