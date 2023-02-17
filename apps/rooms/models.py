from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Currency(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название валюты"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

class Room(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название комнаты"
    )
    description = models.TextField(
        verbose_name="Описание комнаты"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='room_images/',
        verbose_name="Основная фотография",
        blank = True, null = True
    )
    price_day = models.PositiveIntegerField(
        verbose_name="Цена за день"
    )
    currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL,
        null = True, verbose_name="Валюта"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"
        
class Review(models.Model):
    room = models.ForeignKey(
        Room, 
        on_delete=models.CASCADE,
        related_name="room_review",
        verbose_name="Комната"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    text = models.TextField(
        verbose_name="Текст"
    )
    checked = models.BooleanField(
        default=False,
        verbose_name="Проверка"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} {self.text}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

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
    checked = models.BooleanField(
        default=False,
        verbose_name="Проверка"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    arrival_date = models.CharField(
        max_length=255,
        verbose_name="Дата заезда"
    )
    departure_date = models.CharField(
        max_length=255,
        verbose_name="Дата отьезда"
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"