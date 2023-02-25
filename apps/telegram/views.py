from django.shortcuts import render
from django.conf import settings
from telebot import TeleBot, types

from apps.telegram.models import TelegramUser
from apps.telegram.helpers import mail

# Create your views here.
bot = TeleBot(settings.TELEGRAM_TOKEN, threaded=False)

@bot.message_handler(commands=['start'])
def start(message:types.Message):
    TelegramUser.objects.get_or_create(username = message.from_user.username, id_telegram=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name,)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name} {message.chat.id}")

def get_message(message:types.Message):
    mail.title = message.text 
    users = TelegramUser.objects.all()
    for u in users:
        bot.send_message(u.id_telegram, mail.title)
    bot.send_message(message.chat.id, "Рассылка окочена")

@bot.message_handler(commands=['mailing'])
def send_mailing(message:types.Message):
    msg = bot.send_message(message.chat.id, "Тест рассылки: ")
    bot.register_next_step_handler(msg, get_message)

def get_reservation_text(message):
    bot.send_message(-1001605378830, message)

@bot.message_handler()  
def not_found(message:types.Message):
    bot.send_message(message.chat.id, "Я вас не понял")