from django.db import models

from apps.rooms.models import Room

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank = True, null = True
    )
    logo = models.ImageField(
        upload_to="logos/",
        verbose_name="Логотип сайта"
    )
    # phone = models.CharField(
    #     max_length=100,
    #     verbose_name="Телефонный номер"
    # )
    email = models.EmailField(
        verbose_name="Почта",
        blank = True, null = True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank = True, null = True
    )
    address_url = models.URLField(
        verbose_name="Ссылка на адрес",
        blank = True, null = True
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook",
        blank = True, null = True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на instagram",
        blank = True, null = True
    )
    whatsapp = models.URLField(
        verbose_name="Ссылка на WhatsApp",
        blank = True, null = True
    )
    telegram = models.URLField(
        verbose_name="Ссылка на Telegram",
        blank = True, null = True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

class Reservation(models.Model):
    room = models.ForeignKey(
        Room, 
        on_delete=models.SET_NULL,
        related_name="room_reservation",
        null = True
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия"
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    phone_number = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"