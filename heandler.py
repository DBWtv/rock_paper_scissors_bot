from aiogram import Bot, Dispatcher, executor, types
from acces_token import token


API_TOKEN: str = token

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


async def process_start_command(message: types.Message):
    await message.answer('Hello there General Kenobi!')


async def process_help_comand(message: types.Message):
    await message.answer('I am learning to work right now. I will response later!')


async def process_hi_comand(message: types.Message):
    await message.answer(f'Hello there @{message.from_user.username}! This bot have pure functional But for now!')


async def send_echo(message: types.Message):
    await message.reply(message.text)


async def send_photo_echo(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)


async def send_sticker_echo(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)


async def proccess_audio_message(message: types.Message):
    await message.answer(text='Я не умею обрабатывать голосовые сообщения')

dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_comand, commands='help')
dp.register_message_handler(process_hi_comand, commands='say_hi')
dp.register_message_handler(proccess_audio_message, content_types=['voice'])
dp.register_message_handler(send_photo_echo, content_types=['photo'])
dp.register_message_handler(send_sticker_echo, content_types=['sticker'])
dp.register_message_handler(send_echo)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
