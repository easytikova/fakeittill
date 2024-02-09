import telebot
from telebot import types

bot = telebot.TeleBot('6323932642:AAGWDipGksgCZE1Pnri6hblI5EOGIPFwkOU')

@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Найти картину')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Викторина')
    btn3 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn2, btn3)
    mess = f'Здравствуй, <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Найти картину":
        bot.send_message(message.chat.id, "Какие элементы картины вы помните?")
    elif message.text == "Викторина":
        bot.send_message(message.chat.id, "Скоро поиграем!")
    if message.text == "Перейти на сайт":
        bot.send_message(message.chat.id, "Электронная коллекция Эрмитажа")

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "Hello" or "Привет" or "Здравствуй" or "Здравствуйте":
#         bot.send_message(message.chat.id, "Здравствуй!", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('Thomas_Gainsborough_-_Portrait_of_a_Lady_in_Blue_-_WGA8414.jpeg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "Я вас не понимаю:(", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.reply_to(message, 'Эта картина есть в нашей коллекции!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.hermitagemuseum.org/wps/portal/hermitage/explore/artworks/?lng=ru"))
    bot.send_message(message.chat.id, 'Для более подробного изучения перейдите на сайт музея', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('Веб-сайт')
    start = types.KeyboardButton('Старт')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Что вы хотите узнать? Выберете опцию в <u>меню</u>', reply_markup=markup, parse_mode='html')


bot.polling(none_stop=True)
