from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.profiles.views import (
    ShipperViewSet, DriverViewSet, 
    CompanyDriverViewSet, CompanyViewSet
)

router = DefaultRouter()
router.register("shipper", ShipperViewSet)
router.register("company", CompanyViewSet)
router.register("company/driver/", CompanyDriverViewSet)
router.register("", DriverViewSet)

urlpatterns = [
    path("", include(router.urls)),
]