import configparser
import telebot
import logging
import time
import sys
import os

config = configparser.ConfigParser()
config.read("bot/config.ini")
log_dir = config["SCRIPT"]["log_dir"]
if log_dir == "" or log_dir == " ":
    raise Exception('Log_dir in file "bot/config.ini" is null')
log_level = config["SCRIPT"]["log_level"]
if log_level == "" or log_level == " ":
    raise Exception('Log_level in file "bot/config.ini" is null')
print(log_level.lower())
match log_level.lower():
    case "info":
        log_level = logging.INFO
    case "debug":
        log_level = logging.DEBUG
    case _:
        raise Exception(f"Log level not defined, you input log level: {log_level.lower()}")

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
