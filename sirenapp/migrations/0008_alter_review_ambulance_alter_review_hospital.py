# Generated by Django 4.0.5 on 2022-06-30 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sirenapp', '0007_hospital_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ambulance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ambulance_reviews', to='sirenapp.ambulance'),
        ),
        migrations.AlterField(
            model_name='review',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hospital_reviews', to='sirenapp.hospital'),
        ),
    ]
