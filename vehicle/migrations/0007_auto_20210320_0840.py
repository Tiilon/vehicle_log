# Generated by Django 3.1.7 on 2021-03-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_auto_20210320_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='return_condition',
            field=models.CharField(blank=True, choices=[(1, 'Intact'), (2, 'Damaged')], max_length=50, null=True),
        ),
    ]
