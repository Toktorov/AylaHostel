from django.db import models
from django_resized.forms import ResizedImageField

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
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер",
        blank = True, null = True
    )
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
        max_length=1000,
        verbose_name="Ссылка на адрес",
        blank = True, null = True
    )
    backround_image = models.ImageField(
        upload_to="backround_image/",
        verbose_name="Изображение на заднем плане в главной странице",
        null = True
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
    phone_number = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
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

class Gallery(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='gallery_images/',
        verbose_name="Основная фотография",
        blank = True, null = True
    )

    def __str__(self):
        return f"{self.image}"

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерии"

class FAQ(models.Model):
    question = models.CharField(
        max_length=300,
        verbose_name="Вопрос"
    )
    answer = models.TextField(
        verbose_name="Ответ"
    )

    def __str__(self):
        return self.question 

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='news_images/',
        verbose_name="Основная фотография",
        blank = True, null = True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Promotion(models.Model):
    image = models.ImageField(
        upload_to="promotions/",
        verbose_name="Фотография"
    )
    url = models.URLField(
        verbose_name="URL"
    )

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

class Benefit(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание"
    )
    icon = models.ImageField(
        upload_to="icons/",
        verbose_name="Иконка"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

class Team(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='news_images/',
        verbose_name="Основная фотография",
        blank = True, null = True
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name="Полное имя"
    )
    job_title = models.CharField(
        max_length=255,
        verbose_name="Должность"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        
class WeAre(models.Model):
    url = models.URLField(
        verbose_name="Основная ссылка",
        blank=True,null= True
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='where_we_are/',
        verbose_name="Основная фотография",
        blank = True, null = True
    )

    def __str__(self):
        return f"{self.url} -- {self.image}"

    class Meta:
        verbose_name = "Где мы есть ?"
        verbose_name_plural = "Где мы есть ?"