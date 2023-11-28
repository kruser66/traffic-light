import sys
import asyncio
import logging
from textwrap import dedent
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from services.yandex import fetch_city_location, fetch_city_weather
from config.settings import BOT_TOKEN


dp = Dispatcher()


@dp.message(CommandStart())
async def send_welcome_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Узнать погоду")]
        ],
        resize_keyboard=True
    )

    await message.reply(
        text=(
            'Привет, я бот, который может рассказать тебе о погоде.'
            'Нажми на кнопку, чтобы узнать погоду.'
        ),
        reply_markup=keyboard
    )


@dp.message()
async def get_weather(message: Message):

    if message.text == 'Узнать погоду':
        await message.reply('Введите название города')
    else:

        city = message.text
        location = await fetch_city_location(city)
        if not location:
            await message.reply('Город не найден! \nВведите правильное название города')
            return

        weather = await fetch_city_weather(location.latitude, location.longitude)

        await message.reply(
            text=dedent(
                f'''
                Город: {location}

                Температура: {weather['temp']} градусов Цельсия
                Давление: {weather['pressure_mm']} мм рт.ст.
                Скорость ветра : {weather['wind_speed']} м/с
                '''
            )
        )


async def main() -> None:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
