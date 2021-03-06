# Generated by Django 3.1.7 on 2021-03-20 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(blank=True, max_length=250, null=True)),
                ('day_needed', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staffs', to=settings.AUTH_USER_MODEL)),
                ('requested_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'requests',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
