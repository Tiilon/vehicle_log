# Generated by Django 3.1.7 on 2021-03-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210320_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('IN', 'Inactive'), ('AC', 'Active')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('St', 'Staff'), ('M', 'Manager'), ('GM', 'General Manager')], max_length=255, null=True),
        ),
    ]