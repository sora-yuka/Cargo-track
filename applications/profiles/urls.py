from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.profiles.views import (
    BaseProfileViewSet, ViewOtherProfileViewSet, ShipperViewSet, DriverViewSet, CompanyDriverViewSet, CompanyViewSet
)

router = DefaultRouter()
router.register("driver", DriverViewSet)
router.register("shipper", ShipperViewSet)
router.register("company", CompanyViewSet)
router.register("company/driver", CompanyDriverViewSet)
router.register("", ViewOtherProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('<int:pk>/rating/', BaseProfileViewSet.as_view({'post': 'rating'})),
]