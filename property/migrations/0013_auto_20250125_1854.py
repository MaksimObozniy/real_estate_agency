from django.db import migrations


def transfer_and_link_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.iterator():
        if not flat.owner or not flat.owners_phonenumber:
            continue

        owner, _ = Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            defaults={'phonenumber_pure': flat.owner_pure_phone}
        )

        owner.owned_flats.add(flat)
class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),  
    ]

    operations = [
        migrations.RunPython(transfer_and_link_owners),
    ]
