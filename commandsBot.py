from aiogram import Bot, Dispatcher, types
from glob import glob
from random import choice
import random
import menu

API_TOKEN = '6161507050:AAGfJRC2iVDm_s0tfi_GjnSoj3MAF7HLsec'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Хочешь картинку с обезьянкой? 😏\n", reply_markup=menu.mainMenu)

@dp.message_handler()
async def echo(message: types.Message):
    # elif message.text == 'Список команд':
    #     await message.answer('1 ...\n2 ...\n3 ...')
    if message.text == 'Хочу картинку':
        lists = glob('images/*')
        picture = choice(lists)
        photo = open(picture, 'rb')
        await message.answer_photo(photo, caption="")
    elif message.text == 'Хочу гифку':
        lists = glob('gif/*')
        picture = choice(lists)
        photo = open(picture, 'rb')
        await message.answer_video(photo, caption="")
    elif message.text == 'Главное меню':
        await message.answer('Главное меню', reply_markup=menu.mainMenu)
    elif message.text == 'Другое':
        await message.answer('Другое', reply_markup=menu.otherMenu)
    elif message.text == 'Roll':
        await message.answer('1 число: ' + str(random.randint(0, 100)))
        await message.answer('2 число: ' + str(random.randint(0, 100)))
    elif message.text == 'Author':
        await message.answer('Выполнил студент группы ПИН-222, kaissu')
    else:
        await message.reply('Меня таким словам/команде не научили :С\nПопробуйте ввести еще раз\n /start')
