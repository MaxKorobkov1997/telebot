import asyncio
import config
import logging
from aiogram import Bot, Dispatcher
from hendlers import hendlers
from callback import calbak
from bot_start import star

bot = Bot(token='5726485557:AAFQ0lSloWU9Bs4uBgC05w3CJ-xMqvQ7QfM')

async def main():
    dp = Dispatcher()
    dp.include_routers(star,
                       hendlers,
                       calbak)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except:
        KeyboardInterrupt()
