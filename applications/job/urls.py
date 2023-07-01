from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.job.views import JobConfirmApiView, JobOfferApiView, JobViewSet, index


router = DefaultRouter()
router.register('', JobViewSet)

urlpatterns = [
    path('map/', index),
    path('', include(router.urls)),
    path('<int:pk>/order/', JobOfferApiView.as_view()),
    path('confirm/<uuid:code>/', JobConfirmApiView.as_view()),
]