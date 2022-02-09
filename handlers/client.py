from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db
from keyboards import kb_client

# @dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приветствую Вас!',reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Vendor991_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def store_open_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 09:00 до 20:00, Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def place_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'г.Нижний Новгород ул.К.Маркса д.23А') # ,reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['Велосипеды в наличии'])
async def existence_command(message: types.Message):
	await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
	dp.register_message_handler(command_start, commands=['start','help'])
	dp.register_message_handler(store_open_command, commands=['Режим_работы'])
	dp.register_message_handler(place_command, commands=['Расположение_магазина'])
	dp.register_message_handler(existence_command, commands=['Велосипеды_в_наличии'])
