from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.profiles.views import (
    ShipperViewSet, DriverViewSet, CompanyDriverViewSet, CompanyViewSet
)

router = DefaultRouter()
router.register("shipper", ShipperViewSet)
router.register("company", CompanyViewSet)
router.register("company/driver/", CompanyDriverViewSet)
router.register("", DriverViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('<int:pk>/rating/', DriverViewSet.as_view({'post': 'rating'})),
    path('company/<int:pk>/rating/', CompanyViewSet.as_view({'post': 'rating'})),
    path('company/driver/<int:pk>/rating/', CompanyDriverViewSet.as_view({'post': 'rating'})),
]