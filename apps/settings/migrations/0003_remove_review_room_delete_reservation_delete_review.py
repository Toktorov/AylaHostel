# Generated by Django 4.1.5 on 2023-02-11 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_weare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='room',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
