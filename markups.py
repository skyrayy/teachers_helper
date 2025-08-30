from telebot import types
from base import prog_link

def markup1(): #меню учителя 
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton(text="Список учеников")
    but1 = types.KeyboardButton(text="Успеваемость ученика")
    but2 = types.KeyboardButton(text="Техподдержка")
    keyboard.add(but)
    keyboard.add(but1)
    keyboard.add(but2)
    return keyboard

def markup2(): #меню ученика
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton(text="Мои оценки")
    but1 = types.KeyboardButton(text="Техподдержка")
    keyboard.add(but, but1)
    return keyboard

def techpodderjka(): #кнопка техподдержки
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Техподдержка', url=prog_link)
    markup.add(btn)
    return markup

