# Generated by Django 4.0.5 on 2022-07-01 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sirenapp', '0009_alter_trip_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ambulance',
            old_name='availability',
            new_name='available',
        ),
    ]
