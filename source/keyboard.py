from telebot import types

def get_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.KeyboardButton("Посмотреть списки"))
    keyboard.add(types.KeyboardButton("Создать списки"))
    keyboard.add(types.KeyboardButton("Удалить списки"))
    keyboard.add(types.KeyboardButton("Изменить список"))
    return keyboard

def get_number_keyboard(list_count):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for i in range(1, list_count+1):
        keyboard.add(types.KeyboardButton(i))
    return keyboard
    

 