from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

# Основное меню
btnRandPic = KeyboardButton('Хочу картинку')
btnHelp = KeyboardButton('Хочу гифку')
btnOther = KeyboardButton('Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandPic, btnHelp, btnOther)

# Доп. меню
btnRoll = KeyboardButton('Roll')
btnAuthor = KeyboardButton('Author')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRoll, btnAuthor, btnMain)
