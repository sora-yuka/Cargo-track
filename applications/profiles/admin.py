from django.contrib import admin
from applications.profiles.models import ShipperProfile, DriverProfile, BaseProfile

# Register your models here.
admin.site.register(BaseProfile)
admin.site.register(ShipperProfile)
admin.site.register(DriverProfile)