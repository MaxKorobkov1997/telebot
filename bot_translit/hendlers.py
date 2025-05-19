from aiogram import Router

from aiogram.types import Message

from keybord import Links
import globals

hendlers = Router()


@hendlers.message()
async def otv(massage: Message):
    _id = massage.chat.id
    print(_id)
    vheb(str(_id), massage.text)
    if massage.text:
        await massage.answer(text='на какой язык перевести',
                             reply_markup=Links)
    else:
        await massage.answer(text=f"Отправьте текст")


def vheb(a, b):
    globals.seve = a
    globals.text = b
    print(f'{globals.seve} || {globals.text}')
