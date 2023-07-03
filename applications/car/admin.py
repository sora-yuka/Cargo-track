from django.contrib import admin
from applications.car.models import (
    CarInfo, CarBrand, CarDocument, CarEquipment, CarType
)

# Register your models here.

admin.site.register(CarBrand)
admin.site.register(CarType)
admin.site.register(CarDocument)
admin.site.register(CarEquipment)
admin.site.register(CarInfo)