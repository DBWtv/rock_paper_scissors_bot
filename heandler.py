from aiogram import Bot, Dispatcher, executor, types
from acces_token import token


API_TOKEN: str = token

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Hello there General Kenobi!')


@dp.message_handler(commands=['help'])
async def process_help_comand(message: types.Message):
    await message.answer('Text me something and i will resend it to you!')

@dp.message_handler(commands=['say_hi'])
async def process_hi_comand(message: types.Message):
    await message.answer(f'Hello there @{message.from_user.username}! This bot have pur functional But for now!')

@dp.message_handler()
async def send_echo(message: types.Message):
    await message.reply('there is no functional yet')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)