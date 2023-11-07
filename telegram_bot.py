import telebot
from telebot import types

# для работы телеграм бота
token = '6562731087:AAEPgWDoOPt6p3z2GH1pg0IBCPr0PFvRzSU'
chatId = '708789635'

bot = telebot.TeleBot(token)
photo_url = 'https://risovach.ru/upload/2019/09/mem/dzheyson--stethem_219834170_orig_.jpg'

@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Получить Стэтхема'))
    bot.send_message(message.chat.id, f'Здравствуй {message.from_user.first_name}!', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Получить Стэтхема':
        bot.send_photo(message.chat.id, photo=photo_url, caption='Если закрыть глаза становится темно\n(c)Джейсон Стэтхем')

# Функция для отправки уведомления
@bot.message_handler(content_types=['text'])
def send_notification(message):
    bot.send_message(chatId, message)

def run_telegram_bot():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    run_telegram_bot()

