#  pip install pytelegrambotapi
import telebot

list_hi = ['Привет', 'привет']
bot = telebot.TeleBot('6980773673:AAFeWJOTuY_EYM7BsHncR6i_izkhLOAZZ-4')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_support = telebot.types.KeyboardButton(text='помогите мне')
    keyboard.add(button_support)
    bot.send_message(chat_id, 'Я новичок! Помоги мне освоиться на новом месте', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_messages(message):
    bot.send_message(message.from_user.id, 'Я тебя не понимаю /help')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() in list_hi:
        bot.send_message(message.from_user.id, 'Привет, чем я тебе могу помочь?')
    elif message.text.lower() == 'ничем' or message.text == 'Ничем':
        bot.send_message(message.from_user.id, 'Тогда пока')
    elif message.text.lower() == 'помогите мне':
        bot.send_message(message.from_user.id, 'что хотел чудик')
    else:
        bot.send_message(message.from_user.id, 'Говори по русски.')


# запуск бота
bot.polling(non_stop=True, interval=0)
