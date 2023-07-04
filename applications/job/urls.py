from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.job.views import JobCanselApiView, JobCompleteApiView, JobConfirmApiView, JobHistoryViewSet, JobOfferApiView, JobViewSet, index


router = DefaultRouter()
router.register('history', JobHistoryViewSet)
router.register('', JobViewSet)


urlpatterns = [
    path('map/', index),
    path('', include(router.urls)),
    path('<int:pk>/order/', JobOfferApiView.as_view()),
    path('<int:pk>/confirm/<uuid:code>/', JobConfirmApiView.as_view()),
    path('<int:pk>/complete/<uuid:code>/', JobCompleteApiView.as_view()),
    path('<int:pk>/cancel/<uuid:code>/', JobCanselApiView.as_view()),
    ]
