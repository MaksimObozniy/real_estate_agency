# Generated by Django 2.2.24 on 2025-02-10 16:18

from django.db import migrations


def update_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year is not None:
            flat.new_building = flat.construction_year >= 2015
            flat.save(update_fields=['new_building'])

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20250206_2159'),
    ]

    operations = [
        migrations.RunPython(update_new_building),
    ]
