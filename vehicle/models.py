from django.conf import settings
from django.db import models
from django.utils import timezone

CONDITION = {
    (1, 'Intact'),
    (2, 'Damaged')
}


class Vehicle(models.Model):
    brand = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    colour = models.CharField(max_length=250, blank=True, null=True)
    image = models.FileField(upload_to='vehicle/', blank=True, null=True)
    yr_of_manufacture = models.DateTimeField(blank=True, null=True)
    procurement_date = models.DateTimeField(blank=True, null=True)
    registration_number = models.CharField(max_length=250, blank=True, null=True)
    condition = models.CharField(max_length=50, blank=True, null=True, choices=CONDITION)
    branch = models.ForeignKey('Branches', on_delete=models.SET_NULL, blank=True, null=True, related_name='vehicle_branch')
    available = models.BooleanField(default=True, null=True, blank=True)
    on_road = models.BooleanField(default=False)
    sent_for_maintenance = models.BooleanField(default=False, null=True, blank=True)
    last_maintained = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        db_table = 'vehicle'


class Branches(models.Model):
    location = models.CharField(max_length=250, blank=True, null=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='branch_manager', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.location}"

    class Meta:
        db_table = 'branches'


REASON = {
    ('Repairs', 'Repairs'),
    ('Maintenance', 'Maintenance')
}


class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='maintain_vehicle', on_delete=models.SET_NULL, blank=True, null=True)
    reason = models.CharField(max_length=250, blank=True, null=True, choices=REASON)
    date_sent = models.DateTimeField(default=timezone.now)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='maintenance', blank=True, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'maintenance'
        verbose_name= 'Maintenance'
        verbose_name_plural = 'Maintenance'

    def __str__(self):
        return f"{self.vehicle} | {self.date_sent.date()}"


class MaintenanceReturn(models.Model):
    maintenance = models.ForeignKey(Maintenance, related_name='returned_vehicle', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    received_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='maintenance_return', blank=True, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'maintenance_return'
        verbose_name = 'MaintenanceReturn'

    def __str__(self):
        return f"{self.maintenance.vehicle} | {self.date_created.date()}"