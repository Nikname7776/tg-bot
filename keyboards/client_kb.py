from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove


b1= KeyboardButton('/Режим_работы')
b2= KeyboardButton('/Расположение_магазина')
b3= KeyboardButton('/Велосипеды_в_наличии')
# b4=KeyboardButton('Поделиться номером', request_contact=True)
# b5=KeyboardButton('Отправить где я', request_Location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
# LinkButton=InlineKeyboardMarkup(text='Ссылка', url='https://youtube.com')

kb_client.add(b1).add(b2).add(b3)

