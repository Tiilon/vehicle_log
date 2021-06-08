# Generated by Django 3.1.7 on 2021-03-21 13:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0008_auto_20210321_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='staff',
            field=models.ManyToManyField(blank=True, related_name='branch_staff', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='return_condition',
            field=models.CharField(blank=True, choices=[(1, 'Intact'), (2, 'Damaged')], max_length=50, null=True),
        ),
    ]
