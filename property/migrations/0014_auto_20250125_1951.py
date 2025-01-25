from django.db import migrations


def link_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')  
    Owner = apps.get_model('property', 'Owner')  

    for flat in Flat.objects.all():
        if flat.owner and flat.owners_phonenumber:
            # Найти или создать владельца
            owner, created = Owner.objects.get_or_create(
                name=flat.owner,
                phonenumber=flat.owners_phonenumber,
                defaults={'phonenumber_pure': flat.owner_pure_phone}
            )
           
            owner.owned_flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20250125_1854'),  
    ]

    operations = [
        migrations.RunPython(link_flats_to_owners),
    ]
