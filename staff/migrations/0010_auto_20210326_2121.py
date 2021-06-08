# Generated by Django 3.1.7 on 2021-03-26 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0013_auto_20210326_2121'),
        ('staff', '0009_auto_20210322_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='vehicle_assigned',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='request_vehicle', to='vehicle.vehicle'),
        ),
        migrations.AlterField(
            model_name='request',
            name='requested_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests', to='staff.staff'),
        ),
        migrations.AlterField(
            model_name='request',
            name='response',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Decline', 'Decline'), ('Approve', 'Approve')], max_length=200, null=True),
        ),
    ]
