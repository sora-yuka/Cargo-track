from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.profiles.views import ShipperViewSet, DriverViewSet

router = DefaultRouter()
router.register("shipper", ShipperViewSet)
router.register("driver", DriverViewSet)

urlpatterns = [
    path("", include(router.urls))
]