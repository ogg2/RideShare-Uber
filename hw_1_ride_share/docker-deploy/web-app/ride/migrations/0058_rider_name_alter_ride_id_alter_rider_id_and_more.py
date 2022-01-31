# Generated by Django 4.0.1 on 2022-01-31 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0057_auto_20220131_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='name',
            field=models.CharField(default='', max_length=200),
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
