# Generated by Django 4.0.1 on 2022-01-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0042_auto_20220130_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='capacity',
            new_name='capacity_remaining',
        ),
        migrations.AlterField(
            model_name='ride',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rider',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
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