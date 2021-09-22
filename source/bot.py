from keyboard import get_menu_keyboard
from database import get_formatted_lists
import telebot

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def reaction_to_text(message):
    user_id = message.from_user.id
    if message.text.lower() == 'hi':
        bot.send_message(user_id, f"Привет, {message.from_user.first_name}")
    if message.text == "/start":
        bot.send_message(user_id, f"Привет, {message.from_user.first_name}, я бот, умеющий создавать список покупок", 
                         reply_markup=get_menu_keyboard())
    if message.text == 'Посмотреть списки':
        msg, list_count = get_formatted_lists(user_id)
        bot.send_message(user_id, text=msg)
    else:
        bot.send_message(message.from_user.id, "Я не понимаю тебя.")


bot.polling(none_stop=True, interval=0)