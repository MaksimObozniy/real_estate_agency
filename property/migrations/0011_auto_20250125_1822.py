from django.db import migrations
import phonenumbers


def normalize_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats_to_process = Flat.objects.all()
    
    for flat in flats_to_process:
        if flat.owners_phonenumber:
            try:
                phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
                
                if phonenumbers.is_valid_number(phone):
                    flat.owner_pure_phone = phonenumbers.format_number(
                        phone, phonenumbers.PhoneNumberFormat.E164
                    )
                else:
                    flat.owner_pure_phone = None
                    
            except phonenumbers.NumberParseException:
                flat.owner_pure_phone = None
            
            flat.save()
            
class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_flat_owner_pure_phone'), 
    ]

    operations = [
        migrations.RunPython(normalize_phone)
    ]