from keyboard import get_menu_keyboard, get_number_keyboard
from database import get_formatted_lists, get_formatted_list_items
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
    elif message.text == "Создать списки":
        msg = bot.send_message(user_id, 'Укажите название вашего нового списка')
        bot.register_next_step_handler(msg, list_data_answer)
    else:
        bot.send_message(user_id, "Я не понимаю тебя.")


def list_number_answer(message):
    user_id = message.from_user.id
    number = message.text
    bot.send_message(user_id, get_formatted_list_items(user_id, number))


def list_data_answer(message):
    list_data = message.text 

bot.polling(none_stop=True, interval=0)