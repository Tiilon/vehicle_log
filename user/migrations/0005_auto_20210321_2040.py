# Generated by Django 3.1.7 on 2021-03-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210320_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('GM', 'General Manager'), ('M', 'Manager'), ('St', 'Staff')], max_length=255, null=True),
        ),
    ]
