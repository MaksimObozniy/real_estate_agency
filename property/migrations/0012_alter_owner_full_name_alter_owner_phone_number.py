# Generated by Django 5.1.6 on 2025-02-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20250212_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone_number',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]
