# Generated by Django 5.1 on 2024-08-15 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_alter_amenity_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='owener',
            new_name='owner',
        ),
    ]
