import telebot
import requests
from telebot import types

bot = telebot.TeleBot("хотел мой токен? А вот хер те!")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == "/help":
        bot.reply_to(message, 'чтобы получить лисичку напиши /fox, "Лисичка", "Дай лисичку" или склонения для "Лиса"')
    if message.text == "/start":
        bot.reply_to(message, 'я бот, любящий лисичек')

@bot.message_handler(content_types=['text'])
def sendfox(message):
    fox_cmd_list=set(["/fox", "Лиса", "Лисы", "Лису", "Лисичка", "Дай лисичку", "Хочу лисичку", "Лис"])
    LastFM_cmd_list=set(["Тиджой","Дум","ЛастФМ"])
    if message.text in fox_cmd_list:
        response = requests.get('https://randomfox.ca/floof/')
        response.encoding = 'utf-8'
        gen=response.json()['image']
        bot.send_message(message.chat.id,"держи лисисичичечку")
        bot.send_photo(message.chat.id, gen)
    elif message.text in LastFM_cmd_list:
        response = requests.get('https://randomfox.ca/floof/')
        response.encoding = 'utf-8'
        gen=response.json()['image']
        bot.send_message(message.chat.id,"фанату дума и ластфм положена лисисисичичичичечечка")
        bot.send_photo(message.chat.id, gen)
    else:
        bot.send_message(message.from_user.id, "Прости, но я не могу тебе дать лисисичичичечичечку")
bot.infinity_polling()
