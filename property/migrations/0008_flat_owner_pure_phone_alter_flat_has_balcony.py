# Generated by Django 5.1.6 on 2025-02-11 16:23

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='RU', verbose_name='Нормализированный номер телефона'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.BooleanField(blank=True, db_index=True, null=True, verbose_name='Наличие балкона'),
        ),
    ]
