# Generated by Django 3.2.4 on 2021-06-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0024_auto_20210603_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='on_road',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='branches',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='maintenancereturn',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
