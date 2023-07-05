from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from applications.account.login_view import TokenObtainPairView
from applications.account.views import (
    ShipperRegisterAPIView, DriverRegisterAPIView, CompanyDriverRegisterAPIView, CompanyRegisterAPIView,
    UserActivationAPIView, PasswordChangeAPIView, ForgotPasswordAPIView, ForgotPasswordConfirmAPIView, 
)

urlpatterns = [
    path("register/shipper/", ShipperRegisterAPIView.as_view()),
    path("register/driver/", DriverRegisterAPIView.as_view()),
    path("register/company/", CompanyRegisterAPIView.as_view()),
    path("register/company/driver/", CompanyDriverRegisterAPIView.as_view()),
    path("confirm/<uuid:activation_code>/", UserActivationAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("change_password/", PasswordChangeAPIView.as_view()),
    path("forgot_password/", ForgotPasswordAPIView.as_view()),
    path("recovery/confirm/", ForgotPasswordConfirmAPIView.as_view()),
]