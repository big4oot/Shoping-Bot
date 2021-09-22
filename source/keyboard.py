from telebot import types

def get_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.KeyboardButton("Посмотреть списки"))
    keyboard.add(types.KeyboardButton("Создать списки"))
    keyboard.add(types.KeyboardButton("Удалить списки"))
    keyboard.add(types.KeyboardButton("Изменить списки"))
    return keyboard

def get_number_lists(list_count):
    pass