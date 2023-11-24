from bot import bot
import configparser
import logging
import asyncio
import time
import sys
import os

config = configparser.ConfigParser()
config.read("bot/config.ini")

api_hash = config["BOT"]["api_hash"]
if api_hash == "" or api_hash == " ":
    raise Exception('Api_hash in file "bot/config.ini" is null')

try:
    api_id = config["BOT"]["api_id"]
    if api_id == "" or api_id == " ":
        raise Exception('Api_id in file "bot/config.ini" is null')
    api_id = int(api_id)
except TypeError:
    raise Exception('Api_id in file "bot/config.ini" is type error')

log_dir = config["SCRIPT"]["log_dir"]
if log_dir == "" or log_dir == " ":
    raise Exception('Log_dir in file "bot/config.ini" is null')

log_level = config["SCRIPT"]["log_level"]
if log_level == "" or log_level == " ":
    raise Exception('Log_level in file "bot/config.ini" is null')
match log_level.lower():
    case "info":
        log_level = logging.INFO
    case "debug":
        log_level = logging.DEBUG
    case _:
        raise Exception(f"Log level not defined, you input log level: {log_level.lower()}")

version = config["SCRIPT"]["version"]
if version == "" or version == " ":
    raise Exception('Version in file "bot/config.ini" is null')

try:
    os.mkdir(log_dir)
except FileExistsError:
    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"{log_dir}/{time.time()}.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("Initialization and code loading is successful, telegram bot loading.")

asyncio.run(bot.start_bot(api_id=api_id, api_hash=api_hash, version=version, logging=logging))
