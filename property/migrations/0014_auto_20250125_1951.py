from django.db import migrations


def link_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    flats_to_process = Flat.objects.iterator()
    owners_cache = {}

    for flat in flats_to_process:
        if flat.owner and flat.owners_phonenumber:
            owner_key = (flat.owner, flat.owners_phonenumber)

            if owner_key not in owners_cache:
                owner, created = Owner.objects.get_or_create(
                    name=flat.owner,
                    phonenumber=flat.owners_phonenumber,
                    defaults={'phonenumber_pure': flat.owner_pure_phone}
                )

                owners_cache[owner_key] = owner
                
            owners_cache[owner_key].owned_flats.add(flat)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20250125_1854'),
    ]

    operations = [
        migrations.RunPython(link_flats_to_owners),
    ]
