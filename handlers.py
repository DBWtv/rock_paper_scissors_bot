from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, KeyboardButtonPollType
from aiogram.types.web_app_info import WebAppInfo

from environs import Env

Env = Env()
Env.read_env()

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = Env('TOKEN')

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard.add(*(str(i) for i in range(1, 8)))


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: types.Message):
    await message.answer('Экспериментируем со специальными кнопками', reply_markup=keyboard)


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
async def process_cucumber_answer(message: types.Message):
    await message.answer('Да, иногда кажется, что огурцов кошки боятся больше')


# Регистрируем хэндлеры
dp.register_message_handler(process_start_command, commands='start')

dp.register_message_handler(process_cucumber_answer, text='Огурцов 🥒')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)