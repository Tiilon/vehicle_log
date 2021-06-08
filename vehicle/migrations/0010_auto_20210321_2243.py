# Generated by Django 3.1.7 on 2021-03-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0009_auto_20210321_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branches',
            name='staff',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='return_condition',
            field=models.CharField(blank=True, choices=[(2, 'Damaged'), (1, 'Intact')], max_length=50, null=True),
        ),
    ]