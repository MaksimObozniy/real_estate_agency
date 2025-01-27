from django.db import migrations


def transfer_and_link_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    flats_to_process = Flat.objects.iterator()
    owners_cache = {}

    for flat in flats_to_process:
        if flat.owner and flat.owners_phonenumber:
            owner_key = (flat.owner, flat.owners_phonenumber)


            if owner_key not in owners_cache:

                owner, _ = Owner.objects.get_or_create(
                    name=flat.owner,
                    phonenumber=flat.owners_phonenumber,
                    defaults={'phonenumber_pure': flat.owner_pure_phone}
                )
                owners_cache[owner_key] = owner

            owners_cache[owner_key].owned_flats.add(flat)
class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),  
    ]

    operations = [
        migrations.RunPython(transfer_and_link_owners),
    ]
