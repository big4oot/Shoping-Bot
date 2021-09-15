import telebot

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def reaction_to_text(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}")
    if message.text == "/start":
        bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}, я бот, умеющий создавать список покупок")
    else:
        bot.send_message(message.from_user.id, "Не понимаю тебя")

bot.polling(none_stop=True, interval=0)