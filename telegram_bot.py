import telebot
from telebot import types
import config

chatId = telebot.TeleBot(config.chatId)

bot = telebot.TeleBot(config.token)
photo_url = 'https://uznayvse.ru/images/stories2016/uzn_1473155502.jpg'

@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Get Statham'))
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}!', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Get Statham':
        bot.send_photo(message.chat.id, photo=photo_url, caption='If you close your eyes, it gets dark\n(c)Jason Statham')

# Функция для отправки уведомления
@bot.message_handler(content_types=['text'])
def send_notification(message):
    bot.send_message(chatId, message)

def run_telegram_bot():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    run_telegram_bot()
