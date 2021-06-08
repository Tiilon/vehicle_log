# Generated by Django 3.1.7 on 2021-03-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210321_2112'),
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
            field=models.CharField(blank=True, choices=[('M', 'Manager'), ('GM', 'General Manager'), ('St', 'Staff')], max_length=255, null=True),
        ),
    ]