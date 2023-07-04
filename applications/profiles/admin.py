from django.contrib import admin
from applications.profiles.models import ShipperProfile, DriverProfile, BaseProfile, CompanyDriverProfile, CompanyProfile

# Register your models here.
admin.site.register(BaseProfile)
admin.site.register(ShipperProfile)
admin.site.register(DriverProfile)
admin.site.register(CompanyDriverProfile)
admin.site.register(CompanyProfile)