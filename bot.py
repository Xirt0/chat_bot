from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup
from random import randint

from config import TOKEN, TOKEN_OPENAI

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

button_1 = KeyboardButton('Привет')
button_2 = KeyboardButton('Помоги')
button_3 = KeyboardButton('скинь гео')
button_4 = KeyboardButton('ичо')
button_5 = KeyboardButton('пон')

markup = ReplyKeyboardMarkup()
markup.add(button_1, button_3, button_2, button_4, button_5)

win = 0
num_1 = 0
num_2 = 0


@dp.message_handler(commands="start")
async def start_bot(message: types.Message):
    await message.reply('привет я блек пенсил', reply_markup=markup)


@dp.message_handler(commands="inline")
async def start_bot(message: types.Message):
    inline_btn_1 = InlineKeyboardButton('Первая кнопка', callback_data='button1')
    inline_btn_2 = InlineKeyboardButton('Вторая кнопка', callback_data='button2')
    inline_km_1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)

    await message.reply('привет я блек пенсил', reply_markup=inline_km_1)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await  bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка')

@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await  bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата вторая кнопка')


@dp.message_handler(commands="game")
async def start_bot(message: types.Message):
    global win, num_1, num_2

    win = randint(1, 100)
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)

    button_game_1 = KeyboardButton(f'{num_1}')
    button_game_2 = KeyboardButton(f'{num_2}')
    button_game_3 = KeyboardButton(f'{win}')

    markup_2 = ReplyKeyboardMarkup()
    markup_2.add(button_game_1, button_game_2, button_game_3)
    await message.reply('выбери число', reply_markup=markup_2)


@dp.message_handler(content_types='text')
async def echo_bot(message: types.Message):
    global num_1
    global num_2
    global win
    if message.text.lower() == str(num_1):
        await message.answer('не угадал')
    elif message.text.lower() == str(win):
        await message.answer('правильно')
    elif message.text.lower() == str(num_2):
        await message.answer('не угадал')


#  @dp.message_handler(content_types='text')
#  async def echo_bot(message: types.Message):
#      global num_1
#      global num_2
#     global win
#     if message.text.lower() == 'привет':
#         await message.answer('привет')
#     elif message.text.lower() == 'помоги':
#         await message.answer('нет')
#     elif message.text.lower() == 'пон':
#         await message.answer('нипон')
#     elif message.text.lower() == 'ичо':
#         await message.answer('а ничо')


if __name__ == '__main__':
    executor.start_polling(dp)
