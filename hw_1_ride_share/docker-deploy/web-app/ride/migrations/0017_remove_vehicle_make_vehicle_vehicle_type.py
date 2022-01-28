# Generated by Django 4.0.1 on 2022-01-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0016_vehicle_license_plate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='make',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('s', 'Small'), ('l', 'Large')], default='s', max_length=20),
        ),
    ]