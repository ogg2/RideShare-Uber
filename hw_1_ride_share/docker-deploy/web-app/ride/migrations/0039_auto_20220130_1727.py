# Generated by Django 2.2.26 on 2022-01-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0038_alter_ride_id_alter_rider_id_remove_rider_ride_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rider',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]