from aiogram import Router, Bot
from vois_chat import chat_vosi
from aiogram.types.input_file import FSInputFile
import config
from translitir import translate_text
from hendlers import vheb
import globals
import os

calbak = Router()
bot = Bot(token='5726485557:AAFQ0lSloWU9Bs4uBgC05w3CJ-xMqvQ7QfM')


@calbak.callback_query()
async def calback(callback):
    print(f'{globals.seve} нтиемскучв {globals.text} вввв {callback.data}')
    audio_save = f'{globals.seve}.mp3'
    translation = translate_text(globals.text, callback.data)
    chat_vosi(translation, audio_save)
    otk = FSInputFile(path=audio_save)
    await bot.send_message(chat_id=callback.from_user.id,
                           text=translation)
    await bot.send_voice(chat_id=callback.from_user.id,
                         voice=otk)
    await callback.answer()
    os.remove(audio_save)
