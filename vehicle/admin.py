from django.contrib import admin
from .models import *

admin.site.register(Vehicle)
admin.site.register(Maintenance)
admin.site.register(Branches)
admin.site.register(MaintenanceReturn)