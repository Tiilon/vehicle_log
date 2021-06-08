# Generated by Django 3.1.7 on 2021-06-03 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0022_auto_20210603_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='last_maintained',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='reason',
            field=models.CharField(blank=True, choices=[('Maintenance', 'Maintenance'), ('Repairs', 'Repairs')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='condition',
            field=models.CharField(blank=True, choices=[(2, 'Damaged'), (1, 'Intact')], max_length=50, null=True),
        ),
    ]