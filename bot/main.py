import telebot #pip install PyTelegramBotApi
from telebot import types 
import requests #pip install requests
from bs4 import BeautifulSoup #pip install BeautifulSoup4
import myparsefunc
#pip install lxml

import myparsefunc
token = "5337118390:AAHRzuxZoWL-eVteqmirJIEYXa8-AwgB4bE"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
 keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
 keyboard.row('/help', '/образование', '/топпроф')
 text = "Привет я бот который поможет тебе узнать об образовании в москве\n Нажми на /help что бы узнать о моём функционале"
 bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start(message):
 text = "Вот весь мой функционал\n\n"
 text += "/образование - выводит информацию о московском образовании\n\n"
 text += "/топпроф - список лучших и самых востребованных профессий"
 text += "Этот бот смотрит сайты с топовыми вузами и колледжами и показывает вам"
 bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['топпроф'])
def start(message):
 keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
 keyboard.row('/вебразраб', '/аналитик', '/тестировщик', '/назад')
 text = "Список самых востребованных профессий\n\n"
 text += "Веб-разработчик;\nАналитик данных;\nБизнес-аналитик;\nРазработчик С++;\nИнженер по тестированию;\nСпециалист по автоматизации и BIM-проектированию (ТИМ);\nЭксперт по креативному программированию;\nЭксперт по роботам и робототехническим системам."
 bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(commands=['назад'])
def start(message):
 keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
 keyboard.row('/help', '/образование', '/топпроф')
 bot.send_message(message.chat.id, "Кнопочки вернулись назад :)", reply_markup=keyboard)

@bot.message_handler(commands=['вебразраб'])
def start(message):
 text = "Веб-разработчик — это специалист, который создает и поддерживает сайты и приложения. Он может работать как над внешним видом сайта, так и над его внутренней, серверной частью."
 bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['аналитик'])
def start(message):
 text = "Он собирает, обрабатывает, изучает и интерпретирует данные: проводит А/B-тесты, строит модели и проверяет, как пользователи и клиенты реагируют на нововведения."
 bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['тестировщик'])
def start(message):
 text = "Он собирает, обрабатывает, изучает и интерпретирует данные: проводит А/B-тесты, строит модели и проверяет, как пользователи и клиенты реагируют на нововведения."
 bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['образование'])
def start(message):
 keyboard = types.InlineKeyboardMarkup()
 but1 = types.InlineKeyboardButton('1', callback_data='obr1')
 but2 = types.InlineKeyboardButton('2', callback_data='obr2')
 but3 = types.InlineKeyboardButton('3', callback_data='obr3')
 keyboard.add(but1, but2, but3)

 text = "О каком образовании вы хотите узнать?\n"
 text += "1 - бесплатное образование\n"
 text += "2 - Колледжи\n"
 text += "3 - Высшее образование\n"
 text += "Что бы выбрать категорию нажмите на одну из кнопок снизу\n"
 bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'obr1')
def send_obr1(call: types.CallbackQuery):
    bot.answer_callback_query(call.id)
    text = "Бесплатное образование от - <a href='https://www.mos.ru/uslugi/obrazovanie/shkola/'>mos.ru</a>\n"
    text += "Российское образование даёт возможность бесплатно: \n\n"
    text += "Записаться в <a href='https://www.mos.ru/pgu/ru/services/procedure/0/0/7700000000162582077/'>первый класс</a>\n"
    text += "Сделать запись во <a href='https://www.mos.ru/pgu/ru/services/procedure/0/0/7700000000162582079/'>все классы</a>\n"
    text += "\nТак же в москве есть множетво <a href='https://www.mos.ru/pgu/ru/services/procedure/0/0/7700000000162415320/'>бесплатных кружкок и секций</a>\n"
    bot.send_message(call.from_user.id, text, parse_mode="HTML", disable_web_page_preview=True)

@bot.callback_query_handler(func=lambda call: call.data == 'obr2')
def send_obr2(call: types.CallbackQuery):
    bot.answer_callback_query(call.id)
    text = "колледжи отличаются от школ своими направлениями в определенную сферу деятельности ученика, такие как программисты, дизайнеры, архитекторы и т.д.\n"    
    text += "<a href='https://college.edunetwork.ru/77/?page=0'>Лучшие колледжи:</a>\n"
    text += myparsefunc.parcecollege()

    bot.send_photo(call.from_user.id,"https://www.vyatsu.ru/uploads/image/1809/img_5209.jpg")
    bot.send_message(call.from_user.id, text, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == 'obr3')
def send_obr3(call: types.CallbackQuery):
    bot.answer_callback_query(call.id)
    text = "Высшее образование отличается своей своей подготовкой учеников, тут учат специальстов всех профессий которые буду вести мир из настоящего в будующее\n"
    text += "<a href='https://vuz.edunetwork.ru/77/?page=0'>Лучшие вузы:</a>\n"
    text += myparsefunc.parcevuz()
    bot.send_photo(call.from_user.id,"http://cdn.iz.ru/sites/default/files/styles/900x506/public/article-2018-09/TASS_28661863.jpg")
    bot.send_message(call.from_user.id, text, parse_mode="HTML")



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Вот тут все команды - /help :)")

bot.polling(none_stop=True, interval=0)