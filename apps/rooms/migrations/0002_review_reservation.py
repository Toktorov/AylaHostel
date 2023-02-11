# Generated by Django 4.1.5 on 2023-02-11 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Текст')),
                ('checked', models.BooleanField(default=False, verbose_name='Проверка')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_review', to='rooms.room', verbose_name='Комната')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Телефонный номер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_reservation', to='rooms.room')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Брони',
            },
        ),
    ]
