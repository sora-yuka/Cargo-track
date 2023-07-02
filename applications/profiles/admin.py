from django.contrib import admin
from applications.profiles.models import (
    ShipperProfile, DriverProfile, CompanyProfile,
)


admin.site.register(ShipperProfile)
admin.site.register(DriverProfile)
admin.site.register(CompanyProfile)