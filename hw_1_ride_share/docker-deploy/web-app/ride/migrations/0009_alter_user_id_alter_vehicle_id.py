# Generated by Django 4.0.1 on 2022-01-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0008_auto_20220123_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]