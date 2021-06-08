from django.conf import settings
from django.db import models
from django.utils import timezone
from vehicle.models import Branches, Vehicle

RESPONSE = {
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('Canceled', 'Canceled'),
    ('Received', 'Received'),
    ('VehReceived', 'VehReceived'),
}


class Request(models.Model):
    requested_by = models.ForeignKey('Staff', on_delete=models.SET_NULL, related_name='requests', blank=True, null=True)
    reason = models.CharField(max_length=250, blank=True, null=True)
    day_needed = models.DateTimeField(blank=True, null=True)
    response = models.CharField(max_length=200, blank=True, null=True, choices=RESPONSE)
    vehicle_assigned = models.ForeignKey(Vehicle, blank=True, null=True, related_name='request_vehicle', on_delete=models.SET_NULL)
    time_received = models.DateTimeField(blank=True, null=True)
    time_of_return = models.DateTimeField(blank=True, null=True)
    vehicle_issued_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='vehicle_issue', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.requested_by}"

    class Meta:
        db_table = 'requests'
        ordering = ('-created_at',)


class Staff(models.Model):
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='staffs', blank=True, null=True)
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, related_name='staff_branch', blank=True, null=True)

    def __str__(self):
        return f"{self.staff}"