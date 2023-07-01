from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.job.views import JobCanselApiView, JobCompleteApiView, JobConfirmApiView, JobOfferApiView, JobViewSet


router = DefaultRouter()
router.register('', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/order/', JobOfferApiView.as_view()),
    path('confirm/<uuid:code>/', JobConfirmApiView.as_view()),
    path('complete/<uuid:code>/', JobCompleteApiView.as_view()),
    path('cancel/<uuid:code>/', JobCanselApiView.as_view()),
    ]