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
    sleeps = models.CharField(
        max_length=255,
        verbose_name="Спальных мест"
    )
    beds = models.CharField(
        max_length=100,
        verbose_name="Количество кроватей"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='post_images/',
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