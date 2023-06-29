from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from applications.account.views import (
    UserRegisterAPIView, UserActivationAPIView
)

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view()),
    path("confirm/<uuid:activation_code>/", UserActivationAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]