from config.config import load_config

config = load_config('/home/dbw/dev/bots/.env')

print(config.tg_bot.token)