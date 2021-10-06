from keyboard import get_menu_keyboard, get_number_keyboard
from database import get_formatted_lists, get_formatted_list_items, send_new_list, delete_list
import telebot


'''
todo:
- исправить возможность ввода некорректного номера списка
- отображение правильных клавиатур
'''

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def reaction_to_text(message):
    user_id = message.from_user.id
    if message.text.lower() == 'hi':
        bot.send_message(user_id, f"Привет, {message.from_user.first_name}")
    elif message.text == "/start":
        bot.send_message(user_id, f"Привет, {message.from_user.first_name}, я бот, умеющий создавать список покупок", 
                         reply_markup=get_menu_keyboard())
    elif message.text == 'Посмотреть списки':
        msg, list_count = get_formatted_lists(user_id)
        if list_count:
            msg = bot.send_message(user_id, text=msg, reply_markup=get_number_keyboard(list_count))
            bot.register_next_step_handler(msg, list_number_answer)
        else:
            bot.send_message(user_id, "У вас нет списков. Создайте.")
    elif message.text == "Создать список":
        msg = bot.send_message(user_id, 'Для создания списка необходимо на первой строчке указать название. Затем (на второй), перечислить\
                                        пункты списка, отделяя их символом ";" \nНапример: \n\nПродукты: \nхлеб;\nрыба;\nмясо;')
        bot.register_next_step_handler(msg, send_list_data)
    elif message.text == 'Удалить списки':
        msg, list_count = get_formatted_lists(user_id)
        if list_count:
            msg = bot.send_message(user_id, text=msg, reply_markup=get_number_keyboard(list_count))
            bot.register_next_step_handler(msg, delete_list_number_answer)
        else:
            bot.send_message(user_id, "У вас нет списков. Создайте.") 
    elif message.text == "Изменить список":
        pass
    else:
        bot.send_message(user_id, "Я не понимаю тебя.")

def list_number_answer(message):
    user_id = message.from_user.id
    number = message.text
    bot.send_message(user_id, get_formatted_list_items(user_id, number))
    bot.send_message(user_id, 'Выберите действие из меню', reply_markup=get_menu_keyboard())


def delete_list_number_answer(message):
    user_id = message.from_user.id
    number = int(message.text)
    delete_list(number, message.from_user.id)
    if delete_list(number, message.from_user.id):
        bot.send_message(user_id, 'Список успешно удалён!')
    else: 
        bot.send_message(user_id, 'Произошла неуспешная попытка.')
    bot.send_message(user_id, 'Выберите действие из меню', reply_markup=get_menu_keyboard())


def extract_listdata_from_message(text, user_id):
    text = text.replace('\n', '')
    title = text.split(':')[0].strip()
    list_items = text.split(':')[1].strip()
    return title, list_items, user_id


def send_list_data(message):
    title, list_items, user_id = extract_listdata_from_message(message.text, message.from_user.id)
    if send_new_list(title, list_items, user_id):
        bot.send_message(user_id, 'Список успешно добавлен!')
    else: 
        bot.send_message(user_id, 'Произошла неуспешная попытка.')
    bot.send_message(user_id, 'Выберите действие из меню', reply_markup=get_menu_keyboard())
    

bot.polling(none_stop=True, interval=0)