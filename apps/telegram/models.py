from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    id_telegram = models.PositiveBigIntegerField(
        verbose_name="ID телеграм"
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        null=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        null=True
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.id_telegram}"
    
    class Meta:
        verbose_name = "Пользователь телеграмма"
        verbose_name_plural = "Пользователи телеграмма"