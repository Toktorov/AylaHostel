# Generated by Django 4.1.5 on 2023-02-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0014_benefit_promotion_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефонный номер'),
        ),
    ]
