from django.urls import path, include
from applications.car.views import CarInfoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", CarInfoViewSet)

urlpatterns = [
    path("", include(router.urls))
]