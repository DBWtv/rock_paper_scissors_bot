from environs import Env

env = Env()

env.read_env()

bot_token = env('TOKEN')
admin_id = env.int('ADMIN_ID')

