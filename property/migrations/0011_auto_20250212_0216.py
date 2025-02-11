# Generated by Django 5.1.6 on 2025-02-11 22:16

from django.db import migrations


def move_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            full_name = flat.owner,
            phone_number = flat.owners_phonenumber,
            defaults={'normalized_phone': flat.owner_pure_phone} 
        )
        owner.flats.add(flat)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(move_owner)
    ]
