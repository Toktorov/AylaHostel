from django.contrib import admin

from apps.telegram.models import TelegramUser

# Register your models here.
admin.site.register(TelegramUser)