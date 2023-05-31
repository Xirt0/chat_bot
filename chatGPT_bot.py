import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN, TOKEN_OPENAI

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
openai.api_key = TOKEN_OPENAI

dialog = []  # Переменная для сохранения состаяния диалога


@dp.message_handler()
async def handle_message(message: types.Message):
    global dialog  # Объявляем пременную dialog как глобальную, чтобы иметь доступ к ней из функции
    # print(message.text)
    user_input = message.text

    # добавляем сообщение пользователя в диалог
    dialog.append({"role": "user", "content": user_input})

    # Отправляем запрос на модель GPT-3.5 Turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            *dialog
        ]
    )
    # Получаем ответ от модели
    answer = response.choices[0].message.content

    # Добавляем ответ ассистента в диалог
    dialog.append({"role": "assistant", "content": answer})
    # Отправляем ответ пользователю
    await message.reply(answer)


if __name__ == '__main__':
    executor.start_polling(dp)
