from django.shortcuts import render
from django.conf import settings
from telebot import TeleBot, types

from apps.telegram.models import TelegramUser

# Create your views here.
bot = TeleBot(settings.TELEGRAM_TOKEN, threaded=False)

@bot.message_handler(commands=['start'])
def start(message:types.Message):
    TelegramUser.objects.get_or_create(username = message.from_user.username, id_telegram=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name,)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")
    
@bot.message_handler()  
def not_found(message:types.Message):
    bot.send_message(message.chat.id, "Я вас не понял")