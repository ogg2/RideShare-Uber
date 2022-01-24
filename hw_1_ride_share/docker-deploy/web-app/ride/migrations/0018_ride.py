# Generated by Django 4.0.1 on 2022-01-24 13:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0017_remove_vehicle_make_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(choices=[('s', 'Small'), ('l', 'Large')], default='s', max_length=20)),
                ('arrival', models.DateTimeField(default=django.utils.timezone.now)),
                ('num_passengers', models.PositiveIntegerField(default=1)),
                ('destination', models.CharField(help_text='What is your destination?', max_length=200)),
                ('shareable', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('o', 'Open'), ('c', 'Complete'), ('f', 'Confirmed')], default='o', help_text='Ride Status', max_length=1)),
                ('owner', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ride_owner', to='ride.user')),
                ('sharer', models.ManyToManyField(blank=True, default=None, related_name='ride_sharer', to='ride.User')),
            ],
        ),
    ]
