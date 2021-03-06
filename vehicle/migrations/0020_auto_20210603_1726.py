# Generated by Django 3.1.7 on 2021-06-03 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0019_auto_20210603_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='date_brought_back',
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
        migrations.CreateModel(
            name='MaintenanceReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('maintenance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='returned_vehicle', to='vehicle.maintenance')),
                ('received_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='maintenance_return', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MaintenanceReturn',
                'db_table': 'maintenance_return',
            },
        ),
    ]
