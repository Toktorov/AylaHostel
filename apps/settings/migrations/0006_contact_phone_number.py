# Generated by Django 4.1.5 on 2023-02-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_reservation_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default=1, max_length=100, verbose_name='Телефонный номер'),
            preserve_default=False,
        ),
    ]
