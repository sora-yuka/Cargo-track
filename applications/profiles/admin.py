from django.contrib import admin
from applications.profiles.models import ShipperProfile, DriverProfile

# Register your models here.
admin.site.register(ShipperProfile)
admin.site.register(DriverProfile)