# Generated by Django 4.1.5 on 2023-02-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(default=1, max_length=255, verbose_name='Имя пользователя'),
            preserve_default=False,
        ),
    ]
